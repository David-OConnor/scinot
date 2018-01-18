from functools import partial
import math
import sys

import colorama

running_ipython = False
try:
    import IPython
except ModuleNotFoundError:
    pass
else:
    ip = IPython.get_ipython()
    if ip is not None:
        running_ipython = True


# Save the bulitin stdout here, since we'll modify it later.
builtin_stdout = sys.stdout.write


superscript_lookup = {
    '0': '⁰',
    '1': '¹',
    '2': '²',
    '3': '³',
    '4': '⁴',
    '5': '⁵',
    '6': '⁶',
    '7': '⁷',
    '8': '⁸',
    '9': '⁹',
    '-': '⁻',
}


class SciNum:
    """For compatibility with IPython's pretty printer: Contains a string,
    with a __repr__ that allows pretty() to print without quotes, as it would
    if using the string directly."""
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return self.text


def _find_power(number: float) -> int:
    """Helper function."""
    raw_power = math.log10(abs(number))
    power = int(raw_power)

    # Needed to prevent result from being an OOM off.
    if 0 > power != raw_power:
        power -= 1
    return power


def format(number: float, sigfigs: int=4) -> str:
    """Convert a number to a string representation of scientific notation."""
    if not isinstance(number, float) and not isinstance(number, int):
        raise ValueError("The first argument must be a number.")
    if number == 0:
        return "0"
    if not isinstance(sigfigs, int):
        raise ValueError("sigfigs must be an integer.")
    if sigfigs < 1:
        raise ValueError("sigfigs must be greater than or equal to 1.")

    # power is our number's order of magnitude.
    power = _find_power(number)

    # trimmed is the number we're raising to a power of 10.
    trimmed = round(number / 10**power, sigfigs - 1)

    # Don't show the decimal if not required.
    if int(trimmed) == trimmed:
        trimmed = int(trimmed)

    # Don't show the 10 or power if not required.
    if power == 0:
        # return f"{trimmed}"
        return str(trimmed)
    if power == 1:
        # return f"{trimmed} × 10"
        return "{} × 10".format(trimmed)

    # Convert power to unicode superscript.
    power_disp = ''.join([superscript_lookup[digit] for digit in str(power)])

    # return f"{trimmed} × 10{power_disp}"
    return "{} × 10{}".format(trimmed, power_disp)


def _color(scitext: str) -> str:
    colored_text = scitext.replace(" × 10", colorama.Fore.CYAN + " × 10" + colorama.Fore.RESET)
    for power in superscript_lookup.values():
        colored_text = colored_text.replace(power, colorama.Fore.GREEN + power + colorama.Fore.RESET)

    return colored_text


def sciprint(number: float, sigfigs: int=4) -> None:
    """Wrapper around format that, rather than returning a string,
    prints to the console."""
    if running_ipython:
        print(_color(format(number, sigfigs)))
    else:
        print(format(number, sigfigs))


def _overwritten_stdout(sigfigs: int, thresh: int, text: str) -> None:
    """Override standard out, if printing scientific notation with a power
    that exceeds a threshhold."""
    try:
        number = float(text)
    except ValueError:
        builtin_stdout(text)
        return
    if number == 0:  # Catch this here to avoid a math domain error on log10.
        builtin_stdout(text)
        return
    
    # power is our number's order of magnitude.
    power = _find_power(number)

    # Only process if the number's order of magnitude is greater than power_thresh.
    if power >= thresh or power <= -thresh:
        if running_ipython:
            builtin_stdout(_color(format(number, sigfigs)))
        else:
            builtin_stdout(format(number, sigfigs))
    else:
        builtin_stdout(text)


def _print_ipython(sigfigs: int, thresh: int, arg, p, cycle) -> None:
    """Uses IPython's pretty printer to modify output for a qtconsole or notebook;
    stdout doesn't seem to work for them."""
    # power is our number's order of magnitude.
    if arg == 0:  # Catch here to prevent math domain error.
        p.text(IPython.lib.pretty.pretty(arg))
        return
    power = _find_power(arg)

    # Only process if the number's order of magnitude is greater than power_thresh.
    if power >= thresh or power <= -thresh:
        p.text(IPython.lib.pretty.pretty(SciNum(_color(format(arg)))))
    else:
        p.text(IPython.lib.pretty.pretty(arg))


def _normal_ipy_printer(arg, p, cycle) -> None:
    p.text(IPython.lib.pretty.pretty(arg))


def start(sigfigs: int=4, thresh: int=4) -> None:
    """Override stdout and Ipython output, so appropriate numbers are displayed
    in scientific notation."""
    sys.stdout.write = partial(_overwritten_stdout, sigfigs, thresh)
    if not running_ipython:
        return
    
    # We only need to handle IPython separately if in a Qtconsole or Notebook.
    if isinstance(ip, IPython.terminal.interactiveshell.TerminalInteractiveShell):
        return

    text_formatter = ip.display_formatter.formatters['text/plain']
    print_ipython = partial(_print_ipython, sigfigs, thresh)

    text_formatter.for_type(float, print_ipython)
    text_formatter.for_type(int, print_ipython)


def end() -> None:
    """End output overriding."""
    del sys.stdout.write

    if not running_ipython:
        return

    # We only need to handle IPython separately if in a Qtconsole or Notebook.
    if isinstance(ip, IPython.terminal.interactiveshell.TerminalInteractiveShell):
        return

    text_formatter = ip.display_formatter.formatters['text/plain']

    text_formatter.for_type(float, _normal_ipy_printer)
    text_formatter.for_type(int, _normal_ipy_printer)
