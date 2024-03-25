from queue import Queue


if __name__ == "__main__":
    q = Queue()

    for i in range(1, 4):
        q.enqueue(i)
    output = [x for x in q.iterate()]
    assert output == [1, 2, 3], output

    assert q.front() == 1
    assert q.back() == 3
    assert q.dequeue() == 1
    assert q.size() == 2

    q.dequeue()
    for i in range(1, 4):
        q.enqueue(i)
    output = [x for x in q.iterate()]
    assert output == [3, 1, 2, 3], output