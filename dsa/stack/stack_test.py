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


if __name__ == "__main__":
    unittest.main()
