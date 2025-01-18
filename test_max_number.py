import io
import sys

def test_find_max():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    find_max(10, 5)
    assert captured_output.getvalue().strip() == "Максимальное число: 10"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    find_max(4, 8)
    assert captured_output.getvalue().strip() == "Максимальное число: 8"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    find_max(7, 7)
    assert captured_output.getvalue().strip() == "Максимальное число: 7"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    find_max(-2, -5)
    assert captured_output.getvalue().strip() == "Максимальное число: -2"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    find_max(0, -5)
    assert captured_output.getvalue().strip() == "Максимальное число: 0"
