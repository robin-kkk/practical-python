from stack import Stack

def validate_bracket_sequence(seq: str) -> bool:
    open_brackets = "([{"
    closed_brackets = ")]}"

    stack = Stack()
    for bracket in seq:
        if bracket in open_brackets:
            stack.push(bracket)
            continue

        if stack.is_empty() or stack.peek() != open_brackets[closed_brackets.index(bracket)]:
            return False
        stack.pop()

    return stack.is_empty()


if __name__ == "__main__":
    assert validate_bracket_sequence("([{}])") is True
    assert validate_bracket_sequence("(()())") is True
    assert validate_bracket_sequence("{]") is False
    assert validate_bracket_sequence("[()]))()") is False
    assert validate_bracket_sequence("[]{}({})") is True