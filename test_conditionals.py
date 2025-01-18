import io
import sys

def test_check_even_odd():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_even_odd(4)
    assert captured_output.getvalue().strip() == "Число четное"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_even_odd(5)
    assert captured_output.getvalue().strip() == "Число нечетное"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_even_odd(-6)
    assert captured_output.getvalue().strip() == "Число четное"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_even_odd(-1)
    assert captured_output.getvalue().strip() == "Число нечетное"
