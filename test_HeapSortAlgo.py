from unittest import TestCase
from algorithms import sort


class TestHeapSortAlgo(TestCase):
    def test_heapsort(self):
        A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        # sort.heapsort(A)
        sort.min_heap_sort(A)

        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                self.fail("heapsort method fails.")
