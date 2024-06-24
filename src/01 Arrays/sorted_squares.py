"""
Optimized solution for problem 977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Time complexity T = O(N) instead of 'brute force' Nlog(N) version

visit https://leetcode.com/problems/squares-of-a-sorted-array/ for details

"""

import unittest
from typing import List


def sorted_squared(nums: List[int]) -> List[int]:
    """
    Returns sorted array of squared values from input array

    :type nums: List[int]
    :rtype: List[int]
    """

    # check if input data is empty
    nums_len = len(nums)
    if not nums_len:
        return []

    # pre-build an array to return
    res = [0] * nums_len

    # start comparing values from input array borders
    left_index = 0
    right_index = nums_len-1

    # fill result array from the end
    for res_index in reversed(range(nums_len)):
        if abs(nums[left_index]) > abs(nums[right_index]):
            # first value is greater than the last - use it
            res[res_index] = nums[left_index]**2
            # and move left index one position right
            left_index += 1
        else:
            # otherwise we need last value
            res[res_index] = nums[right_index]**2
            # and move right index one position left
            right_index -= 1

    # return squared values array
    return res


class TestSquareAndSort(unittest.TestCase):
    """
    Test cases for an algorithm implementation above
    """
    def test_empty_array(self):
        self.assertEqual(sorted_squared([]), [])

    def test_single_element_array(self):
        self.assertEqual(sorted_squared([2]), [4])

    def test_multiple_element_array(self):
        self.assertEqual(sorted_squared([1, 2, 3, 4]), [1, 4, 9, 16])
        self.assertEqual(sorted_squared([0, 1, 2, 3]), [0, 1, 4, 9])
        self.assertEqual(sorted_squared([5, 6, 7, 8]), [25, 36, 49, 64])

    def test_negative_numbers(self):
        self.assertEqual(sorted_squared([-3, -2, -1, 0]), [0, 1, 4, 9])
        self.assertEqual(sorted_squared([-5, -4, -3]), [9, 16, 25])

    def test_mixed_numbers(self):
        self.assertEqual(sorted_squared([-2, 0, 3, 5]), [0, 4, 9, 25])


# program starting point
if __name__ == '__main__':
    unittest.main()
