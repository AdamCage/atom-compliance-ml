def test_check_simple_method_success():
    expected_data = 3
    actual_data = plus(1, 2)
    assert expected_data == actual_data


def test_check_simple_method_failure():
    expected_data = 3
    actual_data = plus(1, 2)
    assert expected_data != actual_data


def plus(num1: int, num2: int) -> int:
    return num1 + num2
