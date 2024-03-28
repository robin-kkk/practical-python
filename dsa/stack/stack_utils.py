from stack import Stack, ListStack


def validate_bracket_sequence(seq: str) -> bool:
    open_brackets = "([{"
    closed_brackets = ")]}"

    stack = Stack()
    for bracket in seq:
        if bracket in open_brackets:
            stack.push(bracket)
            continue

        if (
            stack.is_empty()
            or stack.peek() != open_brackets[closed_brackets.index(bracket)]
        ):
            return False
        stack.pop()

    return stack.is_empty()


def get_monotonic_increasing_stack(arr: list) -> list:
    stk = ListStack()
    for x in arr:
        while not stk.is_empty() and stk.peek() > x:
            stk.pop()
        stk.push(x)
    return stk.iterate()


def get_monotonic_decreasing_stack(arr: list) -> list:
    stk = ListStack()
    for x in arr:
        while not stk.is_empty() and stk.peek() < x:
            stk.pop()
        stk.push(x)
    return stk.iterate()
