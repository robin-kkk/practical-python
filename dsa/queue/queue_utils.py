from collections import deque


def get_monotonic_increasing_deque(arr: list) -> list:
    dq = deque()
    for x in arr:
        while dq and dq[-1] > x:
            dq.pop()
        dq.append(x)
    return list(dq)


def get_monotonic_decreasing_deque(arr: list) -> list:
    dq = deque()
    for x in arr:
        while dq and dq[-1] < x:
            dq.pop()
        dq.append(x)
    return list(dq)
