# python3


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        #for i in range(len(self._data)):
        #    for j in range(i + 1, len(self._data)):
        #        if self._data[i] > self._data[j]:
        #            self._swaps.append((i, j))
        #            self._data[i], self._data[j] = self._data[j], self._data[i]

        # We have to implement a SiftDown function for any given element index.
        for i in range(len(self._data) // 2, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        min_index = i  # Use minIndex instead of maxIndex cos we're building a min-heap.
        left_child = (2 * i) + 1  # The +1 accounts for the array being zero-indexed.
        # Compare the element with its left child.
        if (left_child < len(self._data) and self._data[left_child] < self._data[min_index]):
            min_index = left_child
        right_child = (2 * i) + 2  # +2 accounts for the array being zero-indexed.
        # Compare the element with its right child.
        if (right_child < len(self._data) and self._data[right_child] < self._data[min_index]):
            min_index = right_child
        # If i now differs from minIndex, swap the two elements in the tree and then
        # call sift_down on the new element.
        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.sift_down(min_index)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
