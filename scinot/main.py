import math


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
        return f"{trimmed}×10"

    # Convert power to unicode superscript.
    power_disp = ''.join([SUPERSCRIPT_LOOKUP[digit] for digit in str(power)])

    return f"{trimmed}×10{power_disp}"