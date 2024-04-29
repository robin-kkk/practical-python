import heapq


# O(nlogn)
def heapsort(arr: list) -> list:
    min_heap = []
    for x in arr:
        heapq.heappush(min_heap, x)
    ans = []
    while min_heap:
        ans.append(heapq.heappop(min_heap))
    return ans


def find_kth_max_element(arr: list, k: int) -> int:
    min_heap = []
    for x in arr:
        heapq.heappush(min_heap, x)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return heapq.heappop(min_heap)


def find_kth_min_element(arr: list, k: int) -> int:
    max_heap = []
    for x in arr:
        heapq.heappush(max_heap, -x)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -heapq.heappop(max_heap)
