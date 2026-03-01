import unittest


def is_subarray(nums1: list[int], nums2: list[int]) -> bool:
    if not nums1:
        return True
    i = 0
    for num in nums2:
        if num == nums1[i]:
            i += 1
            if i == len(nums1):
                return True
    return False


class TestIsSubarray(unittest.TestCase):

    def test_example_1(self):
        self.assertTrue(is_subarray([1, 2, 3], [1, 2, 3, 4]))

    def test_example_2(self):
        self.assertFalse(is_subarray([4, 2], [1, 2, 3, 4]))

    def test_example_3(self):
        self.assertTrue(is_subarray([1, 3, 5], [1, 2, 3, 4, 5]))

    def test_empty_nums1(self):
        self.assertTrue(is_subarray([], [1, 2, 3]))

    def test_equal_arrays(self):
        self.assertTrue(is_subarray([1, 2, 3], [1, 2, 3]))

    def test_nums1_longer_than_nums2(self):
        self.assertFalse(is_subarray([1, 2, 3, 4], [1, 2]))


if __name__ == "__main__":
    unittest.main()