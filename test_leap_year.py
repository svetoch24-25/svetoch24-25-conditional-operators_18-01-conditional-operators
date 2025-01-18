import io
import sys

def test_is_leap_year():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    is_leap_year(2020)
    assert captured_output.getvalue().strip() == "Год високосный"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    is_leap_year(2021)
    assert captured_output.getvalue().strip() == "Год не високосный"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    is_leap_year(2000)
    assert captured_output.getvalue().strip() == "Год високосный"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    is_leap_year(1900)
    assert captured_output.getvalue().strip() == "Год не високосный"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    is_leap_year(0)
    assert captured_output.getvalue().strip() == "Год високосный"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    is_leap_year(1600)
    assert captured_output.getvalue().strip() == "Год високосный"
