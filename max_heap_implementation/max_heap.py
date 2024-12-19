class MaxHeap:
    def __init__(self, heap_size):
        self.heap_size = heap_size
        self.max_heap = [0] * heap_size
        self.real_size = 0

    def add(self, element):
        if self.real_size == self.heap_size:
            print("Too many elements added")
            return

        # element to be inserted in the end
        self.max_heap[self.real_size] = element
        self.real_size += 1

        # heapify up
        index = self.real_size - 1
        parent = (index - 1) // 2
        while index > 0 and self.max_heap[parent] < self.max_heap[index]:
            self.max_heap[parent], self.max_heap[index] = self.max_heap[index], self.max_heap[parent]
            index = parent
            parent = (index - 1) // 2

    def peak(self):
        if self.real_size == 0:
            return None
        return self.max_heap[0]

    def pop(self):
        if self.real_size == 0:
            print("Heap is empty")
            return None

        # pop top element
        popped_element = self.max_heap[0]

        # last element to the root
        self.max_heap[0] = self.max_heap[self.real_size - 1]
        self.max_heap[self.real_size - 1] = 0
        self.real_size -= 1

        #check cond and heapify down
        index = 0
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            #check for left and right children
            if left < self.real_size and self.max_heap[left] > self.max_heap[largest]:
                largest = left

            if right < self.real_size and self.max_heap[right] > self.max_heap[largest]:
                largest = right

            # if largest is not the current node, swap
            if largest != index:
                self.max_heap[index], self.max_heap[largest] = self.max_heap[largest], self.max_heap[index]
                index = largest
            else:
                break

        return popped_element

    def size(self):
        return self.real_size


def main():
    max_heap = MaxHeap(20)
    max_heap.add(2)
    max_heap.add(4)
    max_heap.add(8)
    max_heap.add(6)
    max_heap.add(14)
    max_heap.add(10)
    max_heap.add(36)
    max_heap.add(24)
    max_heap.add(20)
    max_heap.add(16)
    max_heap.add(32)

    print("Initial max heap: \n{}".format(max_heap.max_heap[:max_heap.size()]))
    print("Peak: {}".format(max_heap.peak()))

    print("Add 7 to heap:")
    max_heap.add(7)
    print(max_heap.max_heap[:max_heap.size()])

    print("Pop: {}".format(max_heap.pop()))
    print("After pop:")
    print(max_heap.max_heap[:max_heap.size()])


if __name__ == "__main__":
    main()
