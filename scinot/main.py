import math


def parse(number: float, sigfigs: int=3) -> str:
    """Convert a number to a string representation of scientific notation."""
    if not isinstance(number, float) and not isinstance(number, int):
        raise ValueError("The first argument must be a number.")
    if not isinstance(sigfigs, int):
        raise ValueError("sigfigsust be an integer.")

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

    return f"{trimmed}×10^{power}"