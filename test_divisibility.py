import io
import sys

def test_check_divisibility():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_divisibility(15)
    assert captured_output.getvalue().strip() == "Число делится на 3 и 5"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_divisibility(7)
    assert captured_output.getvalue().strip() == "Число не делится на 3 и 5"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_divisibility(9)
    assert captured_output.getvalue().strip() == "Число не делится на 3 и 5"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_divisibility(0)
    assert captured_output.getvalue().strip() == "Число делится на 3 и 5"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_divisibility(60)
    assert captured_output.getvalue().strip() == "Число делится на 3 и 5"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_divisibility(-15)
    assert captured_output.getvalue().strip() == "Число делится на 3 и 5"

    captured_output = io.StringIO()
    sys.stdout = captured_output
    check_divisibility(-10)
    assert captured_output.getvalue().strip() == "Число делится на 3 и 5"
