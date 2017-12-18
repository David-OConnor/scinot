import math
import sys
from typing import Callable


builtin_print = print
builtin_stdout = sys.stdout.write


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


def parse(number: float, sigfigs: int=3) -> str:
    """Convert a number to a string representation of scientific notation."""
    if not isinstance(number, float) and not isinstance(number, int):
        raise ValueError("The first argument must be a number.")
    if not isinstance(sigfigs, int):
        raise ValueError("sigfigs must be an integer.")

    # power is our number's order of magnitude.
    power = int(math.log10(abs(number)))

    # Needed to prevent result from being an OOM off.
    if power < 0:
        power -= 1

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


def disp(number: float, sigfigs: int=3) -> None:
    """Wrapper around parse that, rather than returning a string,
    prints to the console."""
    builtin_print(parse(number, sigfigs))


def overwritten_print(text, thresh: int=4, sigfigs: int=3) -> None:
    try:
        number = float(text)
    except ValueError:
        builtin_print(text)
        return
    
    power = int(math.log10(abs(number)))

    # Only process if the number's order of magnitude is greater than power_thresh.
    if abs(power) >= thresh:
        disp(number, sigfigs)
    else:
        builtin_print(text)


def overwritten_stdout(text, thresh: int=5, sigfigs: int=3) -> None:
    try:
        number = float(text)
    except ValueError:
        builtin_stdout(text)
        return
    
    power = int(math.log10(abs(number)))

    # Only process if the number's order of magnitude is greater than power_thresh.
    if abs(power) >= thresh:
        disp(number, sigfigs)
    else:
        builtin_stdout(text)

def temp():
    print = overwritten_print
    sys.stdout.write = overwritten_stdout


def start(sigfigs: int=3) -> None:
    """Override the print function, so appropriate numbers are displayed
    in scientific notation."""

    global print
    # global sys.stdout.write

    # builtin_print = print
    # builtin_stdout = sys.stdout.write
    
    # print = partial(_overwritten_disp, __builtins__.print)
    print = _overwritten_disp
    # sys.stdout.write = partial(_overwritten_disp, builtin_stdout)


def end() -> None:
    """End builtin print-overriding."""
    #global print

    del print
    del sys.stdout.write