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


def find_nearest_smaller_element(arr: list) -> list:
    n = len(arr)
    ans = []

    # find the previous and next smaller element for each element.
    prev_smaller = [-1] * n
    next_smaller = [-1] * n
    stk = ListStack()
    for i, x in enumerate(arr):
        while not stk.is_empty() and stk.peek()[0] > x:
            next_smaller[stk.peek()[1]] = x
            stk.pop()
        if not stk.is_empty():
            prev_smaller[i] = stk.peek()[0]
        stk.push((x, i))

    for i in range(n):
        ans.append((prev_smaller[i], next_smaller[i]))
    return ans


def find_nearest_greater_element(arr: list) -> list:
    n = len(arr)
    ans = []

    # find the previous and next greater element for each element.
    prev_greater = [-1] * n
    next_greater = [-1] * n
    stk = ListStack()
    for i, x in enumerate(arr):
        while not stk.is_empty() and stk.peek()[0] < x:
            next_greater[stk.peek()[1]] = x
            stk.pop()
        if not stk.is_empty():
            prev_greater[i] = stk.peek()[0]
        stk.push((x, i))

    for i in range(n):
        ans.append((prev_greater[i], next_greater[i]))
    return ans
