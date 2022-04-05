
#? Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#? Note that you must do this in-place without making a copy of the array.

#! Example 1:
#! Input: nums = [0,1,0,3,12]
#! Output: [1,3,12,0,0]

#! Example 2:
#! Input: nums = [0]
#! Output: [0]

from typing import List

#! bruteforce solution (2534ms runtime on leetcode)
def move_zeroes(nums: List[int]) -> None:
    if len(nums) == 1:
        print(nums)
        
    else:
        zeroes = [0] * nums.count(0)
        while nums.count(0) != 0:
            nums.remove(0)
        nums.extend(zeroes)
        print(nums)
move_zeroes([0,1,0,3,12])
move_zeroes([0])
move_zeroes([0, 0, 1])

#! optimized solution (168 ms runtime on leetcode)
def move_zeroes_2(nums: List[int]) -> None:
    if len(nums) == 1:
        print(nums)
        
    else:
        zeroes = [0] * nums.count(0)
        while nums.count(0) != 0:
            nums.remove(0)
        nums.extend(zeroes)
        print(nums)
move_zeroes_2([0,1,0,3,12])
move_zeroes_2([0])
move_zeroes_2([0, 0, 1])