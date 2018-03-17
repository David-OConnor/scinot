import sys

import pytest

import scinot


def test_long_num():
    assert scinot.format(341283875012.238, 4) == "3.413 × 10¹¹"


def test_short_num():
    assert scinot.format(15, 4) == "1.5 × 10"


def test_tiny_num():
    assert scinot.format(.0000098326543, 6) == "9.83265 × 10⁻⁶"


def test_lower_sigfigs():
    assert scinot.format(.0000098326543, 3) == "9.83 × 10⁻⁶"


def test_neg_num():
    assert scinot.format(-8328389, 1) == "-8 × 10⁶"


def test_0_sigfigs():
    # disply scinot with standard number and 0 as digits count

    with pytest.raises(ValueError):
        scinot.format(1234567890, 0)


# todo: Test std output.
