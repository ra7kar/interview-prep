# Creating a minheap.
# a array is used to represent a heap.

from collections import deque


class MinHeap:
    def __init__(self, list):
        self.min_heap = deque()
        self.count = 0
        for i in list:
            self.add_min_heap(i)

    def add_min_heap(self, element):

        self.min_heap.append(element)
        self.count += 1
        new_element_index = len(self.min_heap) - 1

        if self.count > 1:
            self.swap_heap(new_element_index)

    def swap_heap(self, new_element_index):
        # bubble up

        if new_element_index != 0:
            parent_index = int((new_element_index - 1) / 2)
            left_index = self.get_left_index(parent_index)
            right_index = self.get_right_index(parent_index)

            parent_value = self.get_val(parent_index)
            left_value = self.get_val(left_index)
            right_value = self.get_val(right_index)

            if left_value is not None and parent_value > left_value:
                self.min_heap[parent_index], self.min_heap[left_index] = (
                    self.min_heap[left_index],
                    self.min_heap[parent_index],
                )

            if right_value is not None and parent_value > right_value:
                self.min_heap[parent_index], self.min_heap[right_index] = (
                    self.min_heap[right_index],
                    self.min_heap[parent_index],
                )

            self.swap_heap(
                parent_index
            )  # loop with parent index till start of index is reached

    def get_val(self, index):
        if len(self.min_heap) - 1 >= index:
            return self.min_heap[index]
        else:
            return None

    def get_left_index(self, parent_index):

        # left child = 2i + 1, i = index of parent
        left_child_index = (2 * parent_index) + 1
        return left_child_index

    def get_right_index(self, parent_index):

        # right child = 2i + 2, i = index of parent
        right_child_index = (2 * parent_index) + 2
        return right_child_index

    def get_parent(self):
        pass

    def heap_print(self):
        list = []
        for i in self.min_heap:
            list.append(i)

        return list

    def pop_min_heap(self, sorted_list):
        # sink down

        sorted_list.append(self.min_heap.popleft())

        # move last element to first
        if len(self.min_heap) != 0:
            last_element = self.min_heap.pop()
            self.min_heap.appendleft(last_element)

            # perform sink down
            self.sink_down(0)

        return sorted_list

    def sink_down(self, parent_index):
        left_index = self.get_left_index(parent_index)
        right_index = self.get_right_index(parent_index)
        left_value = self.get_val(left_index)
        right_value = self.get_val(right_index)
        parent_value = self.get_val(parent_index)

        if right_value is None or left_value < right_value:
            swap_value = left_value
            swap_index = left_index
        else:
            swap_value = right_value
            swap_index = right_index

        if left_value is not None and parent_value > swap_value:
            self.min_heap[parent_index], self.min_heap[swap_index] = (
                self.min_heap[swap_index],
                self.min_heap[parent_index],
            )
            parent_index = swap_index
        else:
            return

        self.sink_down(parent_index)

    def sorted_list(self, sorted_list):
        for i in range(len(self.min_heap)):
            self.pop_min_heap(sorted_list)

        return sorted_list


def main():

    py_list = [4, 5, 6, 7, 1, 2, 3]
    #    l = [3,5,7,1,5,8,2,1]
    sorted_list = []

    print(py_list)
    min_heap = MinHeap(py_list)

    print("Min Heap ------")
    print(min_heap.heap_print())
    min_heap.sorted_list(sorted_list)
    print(sorted_list)
    print(min_heap.heap_print())


if __name__ == "__main__":
    main()
