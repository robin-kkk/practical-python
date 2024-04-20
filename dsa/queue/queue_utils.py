from collections import deque


def get_monotonic_increasing_deque(arr: list) -> list:
    n = len(arr)
    dq = deque()
    for i in range(n):
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()
        dq.append(i)
        # print(f'The minimum value when going through arr[0:{i}]: {arr[dq[0]]}')
    return [arr[i] for i in dq]


def get_monotonic_decreasing_deque(arr: list) -> list:
    n = len(arr)
    dq = deque()
    for i in range(n):
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        # print(f'The maximum value when going through arr[0:{i}]: {arr[dq[0]]}')
    return [arr[i] for i in dq]


def find_minimum_value_of_window(arr: list, k: int) -> list:
    n = len(arr)
    dq = deque()
    ans = []
    for i in range(n):
        # Expand the window to the right.
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()
        dq.append(i)
        # Shrink the window from the left.
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Find the minimum.
        if i >= k - 1:
            ans.append(arr[dq[0]])
    return ans


def find_maximum_value_of_window(arr: list, k: int) -> list:
    n = len(arr)
    dq = deque()
    ans = []
    for i in range(n):
        # Expand the window to the right.
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        # Shrink the window from the left.
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Find the maximum.
        if i >= k - 1:
            ans.append(arr[dq[0]])
    return ans
