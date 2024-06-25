"""
Optimized solution for problem 896. Monotonic Array

An array is monotonic if it is either monotone increasing
or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic,
or false otherwise.

Time complexity is O(N)
Space complexity is O(1)

visit https://leetcode.com/problems/monotonic-array/ for details

"""

import unittest
from typing import List


def is_monotonic(nums: List[int]) -> bool:
    """
    Checks if given array is monotonic

    :type nums: List[int]
    :rtype: bool
    """

    # first, check "edge cases"
    nums_len = len(nums)
    if nums_len < 2:
        return True

    if nums[0] < nums[-1]:
        # this array can be monotonic only if it is monotonic increasing
        for index in range(nums_len-1):
            if nums[index] > nums[index+1]:
                # next element lesser than previous
                return False
    elif nums[0] > nums[-1]:
        # this array can be monotonic only if it is monotonic decreasing
        for index in range(nums_len - 1):
            if nums[index] < nums[index + 1]:
                # next element bigger than previous
                return False
    else:
        # all number should be equal for this array to be monotonic
        for index in range(1, nums_len):
            if nums[index] != nums[0]:
                return False

    return True


class TestIsMonotonic(unittest.TestCase):
    """
    Test cases for an algorithm implementation above
    """

    def test_monotonic_array(self):
        # Test for increasing monotonic array
        self.assertTrue(
            is_monotonic(
                [1, 2, 3, 4, 5]
            )
        )

        # Test for decreasing monotonic array
        self.assertTrue(
            is_monotonic(
                [5, 4, 3, 2, 1]
            )
        )

        # Test for non-monotonic array
        self.assertFalse(
            is_monotonic(
                [1, 3, 2, 4, 5]
            )
        )

        # Test for monotonic array
        self.assertTrue(
            is_monotonic(
                [1, 1, 1, 1, 1]
            )
        )

        # Test for non-monotonic array
        self.assertFalse(
            is_monotonic(
                [1, 1, 8, 1, 1]
            )
        )

        # Test for empty array
        self.assertTrue(
            is_monotonic(
                []
            )
        )

        # Test for array with a single element
        self.assertTrue(
            is_monotonic(
                [1]
            )
        )


# program starting point
if __name__ == '__main__':
    unittest.main()
