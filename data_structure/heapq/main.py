import heapq

if __name__ == "__main__":
    """
    the heapq module implements a min heap, but you can implement a max heap by negating the values before adding them to the heap and negating them again when extracting the maximum value
    """

    #  min heap
    print("============ min heap ============")
    min_heap = []
    heapq.heappush(min_heap, 2)
    heapq.heappush(min_heap, -1)
    heapq.heappush(min_heap, 0)
    heapq.heappush(min_heap, -5)
    heapq.heappush(min_heap, 10)
    heapq.heappush(min_heap, -10)

    print(min_heap)
    print(heapq.heappop(min_heap))

    # use heapify
    data = [100, -9, 7, -2, -20, 95]
    heapq.heapify(data)
    print(data)

    print()
    print("============ max heap ============")
    # [-10, -1, -5, 2, 30, 0]
    max_heap = []
    heapq.heappush(max_heap, -(-10))
    heapq.heappush(max_heap, -(-1))
    heapq.heappush(max_heap, -(-5))
    heapq.heappush(max_heap, -(2))
    heapq.heappush(max_heap, -(30))
    heapq.heappush(max_heap, (0))
    print(max_heap)
