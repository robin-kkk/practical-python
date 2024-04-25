class PriorityQueue:

    def __init__(self, arr: list[object] = [], comparator: object = None):
        self._size = 0
        self._capacity = len(arr)
        self._heap = []
        self._map = dict()
        # _higher(x, y) is the comparator that returns whether x has higher priority than y.
        self._higher = comparator or (lambda x, y: x < y)

        for obj in arr:
            self.add(obj)

        # for i in range(max(0, int(self._size / 2) - 1), -1, -1):
        #     self._sink_down(i)

    def _add_map(self, obj: object, at: int) -> None:
        if obj not in self._map:
            self._map[obj] = set()
        self._map[obj].add(at)
        return None

    def _remove_map(self, obj: object, at: int) -> None:
        self._map[obj].remove(at)
        if len(self._map[obj]) == 0:
            self._map.pop(obj)
        return None
    
    def _swap(self, i: int, j: int) -> None:
        o1, o2 = self._heap[i], self._heap[j]
        self._map[o1].remove(i)
        self._map[o1].add(j)
        self._map[o2].remove(j)
        self._map[o2].add(i)
        self._heap[i], self._heap[j] = o2, o1
        return None
    
    def _swim_up(self, at: int) -> None:
        parent = int((at - 1) / 2)
        while at > 0 and self._higher(self._heap[at], self._heap[parent]):
            self._swap(parent, at)
            at = parent
            parent = int((at - 1) / 2)
        return None
    
    def _sink_down(self, at: int) -> None:
        while True:
            candidate = at
            l, r = at*2 + 1, at*2 + 2
            
            # Choose the smallest child node.
            left_child = self._heap[l] if l < self._size else None
            if left_child and self._higher(left_child, self._heap[candidate]):
                candidate = l
            
            right_child = self._heap[r] if r < self._size else None
            if right_child and self._higher(right_child, self._heap[candidate]):
                candidate = r
            
            if candidate == at:
                break
            
            self._swap(candidate, at)
            at = candidate
            
        return None
    
    def peek(self):
        if self.is_empty():
            raise Exception('PriorityQueue is empty.')
        return self._heap[0]

    def poll(self) -> object:
        if self.is_empty():
            raise Exception('PriorityQueue is empty.')
        return self.remove_at(0)
        
    def add(self, obj: object) -> None:
        # Append it to the end of our heap.
        self._heap.append(obj)
        # Add it into our hash table (Its key happens to be the last index + 1).
        self._add_map(obj, self._size)
        # Swim up the node at the last position.
        self._swim_up(self._size)
        # Increment the number of nodes. 
        self._size += 1
        # Do doubling the capacity if the size exceeds it.
        if self._size > self._capacity:
            self._capacity *= 2

    def remove_at(self, at: int) -> object:
        if self.is_empty():
            raise Exception('PriorityQueue is empty.')
        
        # Decrement the number of nodes.
        self._size -= 1
        # Swap the given node with the last one.
        self._swap(at, self._size)
        # Remove the last node.
        removed = self._heap[self._size]
        self._remove_map(removed, self._size)
        self._heap.pop()

        # Early return if it removed the last one.
        if at == self._size:
            return removed

        # Try sinking down or swimming up. 
        prev_last_obj = self._heap[at]
        self._sink_down(at)
        if self._heap[at] == prev_last_obj:
            self._swim_up(at)

        return removed
    
    def remove(self, obj: object) -> object:
        if self.is_empty():
            raise Exception('PriorityQueue is empty.')
        # The first position where a given object occurs.
        at = self._map[obj].pop()
        # Restore it to make removal operation correct.
        self._map[obj].add(at)
        return self.remove_at(at)

    def contain(self, obj: object) -> bool:
        return obj in self._map

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def clear(self) -> None:
        self._size = 0
        self._capacity = 0
        self._heap.clear()
        self._map.clear()
    
    def validate_heap_property(self, i: int) -> bool:
        if i >= self._size:
            return True
        l, r = i*2 + 1, i*2 + 2
        if l < self._size and self._higher(self._heap[l], self._heap[i]):
            return False
        if r < self._size and self._higher(self._heap[r], self._heap[i]):
            return False
        return self.validate_heap_property(l) and self.validate_heap_property(r)
