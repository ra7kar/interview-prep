# Implement Heaps with a list
#


class MinHeap:
    def __init__(self, arr=[]):
        self.min_heap = []
        for data in arr:

            if self.min_heap is None:
                self.min_heap.append(data)
            else:
                self.add_node(data)

    def add_node(self, data):

        self.min_heap.append(data)
        child_index = len(self.min_heap) - 1
        parent_index = self.get_parent_index(child_index)
        while self.min_heap[parent_index] > self.min_heap[child_index]:
            child_index = self.swap(child_index, parent_index)
            parent_index = self.get_parent_index(child_index)

    def swap(self, child_index, parent_index=None, for_swap=False):
        if parent_index is None:
            parent_index = self.get_parent_index(child_index)
        if self.min_heap[parent_index] > self.min_heap[child_index] or for_swap:
            self.min_heap[parent_index], self.min_heap[child_index] = (
                self.min_heap[child_index],
                self.min_heap[parent_index],
            )
        return parent_index

    def get_left_child_index(self, parent_index):
        child_index = parent_index * 2 + 1
        return child_index if child_index != 0 else 0

    def get_right_child_index(self, parent_index):
        right_index = parent_index * 2 + 2
        return right_index if right_index != 0 else 0

    def get_parent_index(self, child_index):
        parent_index = int((child_index - 1) / 2)

        return parent_index if parent_index != 0 else 0

    def get_heap(self):
        return self.min_heap

    def get_root(self):
        return self.root

    def pop(self):

        ret_val = self.min_heap[0]
        child_index = len(self.min_heap) - 1
        parent_index = 0
        self.swap(child_index, parent_index, True)
        self.min_heap.pop(child_index)
        self.heapify()

        return ret_val

    def get_val(self, position):
        return self.min_heap[position]

    def heapify(self):

        parent_index = 0

        left_child_index = self.get_left_child_index(parent_index)
        right_child_index = self.get_right_child_index(parent_index)

        def helper_heapify(parent_index, left_child_index, right_child_index):

            if 0 < left_child_index < len(self.min_heap) - 1:

                parent_val = self.get_val(parent_index)
                left_val = self.get_val(left_child_index)
                right_val = self.get_val(right_child_index)
                swap_val = min(left_val, right_val)
                swap_index = (
                    left_child_index if swap_val == left_val else right_child_index
                )

                if parent_val > swap_val:
                    self.swap(swap_index, parent_index, True)
                    new_left_child_index = self.get_left_child_index(swap_index)
                    new_right_child_index = self.get_right_child_index(swap_index)

                    helper_heapify(
                        swap_index, new_left_child_index, new_right_child_index
                    )

        helper_heapify(parent_index, left_child_index, right_child_index)


def main():

    arr = [50, 10, 45, 20, 30, 60, 22, 32, 12, 5]
    heap = MinHeap(arr)
    print("-" * 25)
    print("Original array")
    print(arr)
    print("-" * 25)
    print("Min Heap array")
    print(heap.get_heap())
    print("-" * 25 + " Root ")
    print(heap.get_heap()[0])
    print("-" * 25 + " Pop ")
    print(heap.pop())
    print("-" * 25 + " New heap ")
    print(heap.get_heap())
    heap.heapify()
    print("-" * 25 + " Heapify ")
    print(heap.get_heap())
    print("-" * 25 + " Pop ")
    print(heap.pop())
    print(heap.get_heap())
    print("-" * 25 + " Add New Node ")
    heap.add_node(4)
    print(heap.get_heap())

    print("-" * 25 + " Pop ")
    print(heap.pop())
    print(heap.get_heap())


if __name__ == "__main__":
    main()
