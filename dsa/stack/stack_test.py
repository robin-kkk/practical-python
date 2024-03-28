import unittest

from stack import Stack, ListStack
import stack_utils


class TestStack(unittest.TestCase):
    def test_stack(self) -> None:
        stack = Stack()
        for elem in ["1", "2", "3", "4"]:
            stack.push(elem)
        assert stack.peek() == "4"
        assert stack.contain("2") is True
        assert stack.remove("2") is True
        assert stack.remove("10") is False
        assert stack.pop() == "4"
        assert stack.pop() == "3"
        assert stack.pop() == "1"
        assert stack.is_empty() is True

    def test_list_stack(self) -> None:
        stack = ListStack()
        for elem in ["1", "2", "3", "4"]:
            stack.push(elem)
        assert stack.peek() == "4"
        assert stack.contain("2") is True
        assert stack.remove("2") is True
        assert stack.remove("10") is False
        assert stack.pop() == "4"
        assert stack.pop() == "3"
        assert stack.pop() == "1"
        assert stack.is_empty() is True

    def test_validate_bracket_sequence(self) -> None:
        assert stack_utils.validate_bracket_sequence("([{}])") is True
        assert stack_utils.validate_bracket_sequence("(()())") is True
        assert stack_utils.validate_bracket_sequence("{]") is False
        assert stack_utils.validate_bracket_sequence("[()]))()") is False
        assert stack_utils.validate_bracket_sequence("[]{}({})") is True

    def test_get_monotonic_increasing_stack(self) -> None:
        # (arr, expected_result)
        tc = [
            ([3, 2, 4, 1, 5, 7], [1, 5, 7]),
            ([2, 5, 3, 8, 7], [2, 3, 7]),
        ]

        for arr, expected_result in tc:
            assert stack_utils.get_monotonic_increasing_stack(arr) == expected_result

    def test_get_monotonic_decreasing_stack(self) -> None:
        # (arr, expected_result)
        tc = [
            ([3, 2, 4, 7, 5, 1], [7, 5, 1]),
            ([6, 4, 7, 1, 8, 3], [8, 3]),
        ]

        for arr, expected_result in tc:
            assert stack_utils.get_monotonic_decreasing_stack(arr) == expected_result


if __name__ == "__main__":
    unittest.main()
