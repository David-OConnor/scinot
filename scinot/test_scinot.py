import scinot
import sys

def test_start_end_sequence(capsys):

    # start scinot for standard prompt input
    print(12345678)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "12345678\n"

    # currently testing empty result as I couldn't find a way to collect stdout of the function
    scinot.start()
    print(12345678)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == ""  # should be "1.235 × 10⁷"


    # end scinot for standard prompt input
    scinot.end()
    print(12345678)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "12345678\n"

def test_disp(capsys):
    # disply scinot with a standard number
    scinot.disp(1234567890)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "1.235 × 10⁹\n"

    # disply scinot with a decimal fraction
    scinot.disp(0.000000001)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "1 × 10⁻⁹\n"

    # disply scinot with a standard number and controlled amount of significant figures
    scinot.disp(1234567890, 7)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "1.234568 × 10⁹\n"

    # disply scinot with standard number and 0 as digits count
    scinot.disp(1234567890, 0)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "0 × 10⁹\n"  # TODO I would expect and error message for amount of significant figures <= 0

    # disply scinot with a negative number
    scinot.disp(-1234567890)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "-1.235 × 10⁹\n"

    # disply scinot with a negative number and controlled amount of significant figures
    scinot.disp(-1234567890,2)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "-1.2 × 10⁹\n"

    # disply scinot with a negative number and controlled amount of significant figures
    scinot.disp(-.00000409348, 2)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == "-4.1 × 10⁻⁶\n"

def test_format(capsys):

    # currently testing empty result as I couldn't find a way to collect stdout of the function

    # disply scinot with a standard number
    scinot.format(1234567890)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == ""  # should be "1.235 × 10⁹\n"

    # disply scinot with a decimal fraction
    scinot.format(0.000000001)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == ""  # should be "1.235 × 10⁹\n"

    # disply scinot with a standard number and controlled amount of significant figures
    scinot.format(1234567890, 7)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == ""  # should be ""1.234568 × 10⁹\n"

    # disply scinot with standard number and 0 as digits count
    scinot.format(1234567890, 0)
    sys.stderr.write("error\n")
    out, err = capsys.readouterr()
    assert out == ""  # should be "0 × 10⁹\n" # TODO I would expect and error message for amount of significant figures <= 0
