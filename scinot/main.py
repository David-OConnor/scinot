from functools import partial
import math
import sys
from typing import Callable

ipython_exists = True
try:
    import IPython, ipykernel.iostream
except ModuleNotFoundError:
    ipython_exists = False


# Save the bulitin stdout and print here, since we'll modify them later.
# builtin_print = print
builtin_stdout = sys.stdout.write

if ipython_exists:
    ipython_stdout = IPython.sys.stdout.write
    ipyout = ipykernel.iostream.OutStream.write

SUPERSCRIPT_LOOKUP = {
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
    if not isinstance(sigfigs, int):
        raise ValueError("sigfigs must be an integer.")

    # power is our number's order of magnitude.
    power = _find_power(number)

    # trimmed is the number we're raising to a power of 10.
    trimmed = round(number / 10**power, sigfigs - 1)

    # Don't show the decimal if not required.
    if int(trimmed) == trimmed:
        trimmed = int(trimmed)

    # Don't show the 10 or power if not required.
    if power == 0:
        return f"{trimmed}"
    if power == 1:
        return f"{trimmed} × 10"

    # Convert power to unicode superscript.
    power_disp = ''.join([SUPERSCRIPT_LOOKUP[digit] for digit in str(power)])

    return f"{trimmed} × 10{power_disp}"


def disp(number: float, sigfigs: int=4, display_func=print) -> None:
    """Wrapper around format that, rather than returning a string,
    prints to the console."""
    display_func(format(number, sigfigs))


# def _overwritten_print(sigfigs: int, thresh: int, *objects,
#                        sep='', end='\n', file=sys.stdout, flush=False) -> None:
#     """This function makes sure that if we don't use scientific notation, print's
#     extra argument are passed to the builtin print."""
#     # builtin_print("TT")
#     text = objects[0]  # todo Handle multiple items?
#
#     try:
#         number = float(text)
#     except ValueError:
#         print(*objects, sep, end, file, flush)
#         return
#
#     # power is our number's order of magnitude.
#     power = _find_power(number)
#
#     # Only process if the number's order of magnitude is greater than power_thresh.
#     if power >= thresh or power <= -thresh:
#         disp(number, sigfigs)
#     else:
#         print(*objects, sep, end, file, flush)


def _overwritten_stdout(sigfigs: int, thresh: int, text: str) -> None:
    """Override a display func like stdout or print."""
    try:
        number = float(text)
    except ValueError:
        builtin_stdout(text)
        return
    
    # power is our number's order of magnitude.
    power = _find_power(number)

    # Only process if the number's order of magnitude is greater than power_thresh.
    if power >= thresh or power <= -thresh:
        disp(number, sigfigs, builtin_stdout)
    else:
        builtin_stdout(text)


def start(sigfigs: int=4, thresh: int=4) -> None:
    """Override the print function, so appropriate numbers are displayed
    in scientific notation."""
    # global print
    # print = partial(_overwritten_print, sigfigs, thresh)
    sys.stdout.write = partial(_overwritten_stdout, sigfigs, thresh)
    # if ipython_exists:
        # ipykernel.iostream.OutStream.write = partial(_overwritten_func, ipyout, sigfigs, thresh)
        # IPython.sys.stdout.write = partial(_overwritten_func, ipython_stdout, sigfigs, thresh)


def end() -> None:
    """End builtin print-overriding."""
    # global print
    # print = builtin_print
    del sys.stdout.write