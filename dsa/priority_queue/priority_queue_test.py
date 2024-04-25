import unittest

from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    
    def test_priority_queue(self) -> None:
        arr = ['banana', 'apple', 'blackberry', 'cherry', 'blueberry', 'avocado']
        pq = PriorityQueue(arr)
        assert pq.poll() == 'apple'
        assert pq.peek() == 'avocado'
        assert pq.remove('blueberry') == 'blueberry'
        assert pq.contain('blueberry') is False
        
        pq.add('tomato')
        pq.add('coconut')
        assert pq.remove('blackberry') == 'blackberry'
        assert pq.remove('cherry') == 'cherry'
        assert pq.size() == 4
        
        result = [pq.poll() for _ in range(pq.size())]
        assert result == ['avocado', 'banana', 'coconut', 'tomato'], result
    
    def test_min_priority_queue(self) -> None:
        testcases = [
            ([1], [1]),
            ([4, 7, 8, 2, 1], [1, 2, 4, 7, 8]),
            ([4, 5, 2, 4, 1, 4, 7, 3], [1, 2, 3, 4, 4, 4, 5, 7]),
        ]
        
        for arr, expected_result in testcases:
            min_pq = PriorityQueue(arr=arr)
            assert min_pq.validate_heap_property(0) is True
            result = [min_pq.poll() for _ in range(len(arr))]
            assert result == expected_result

    def test_max_priority_queue(self) -> None:
        testcases = [
            ([1], [1]),
            ([4, 7, 8, 2, 1], [8, 7, 4, 2, 1]),
            ([4, 5, 2, 4, 1, 4, 7, 3], [7, 5, 4, 4, 4, 3, 2, 1]),
        ]
        
        for arr, expected_result in testcases:
            max_pq = PriorityQueue(arr=arr, comparator=lambda x, y: x > y)
            assert max_pq.validate_heap_property(0) is True
            result = [max_pq.poll() for _ in range(len(arr))]
            assert result == expected_result

    
if __name__ == "__main__":
    unittest.main()