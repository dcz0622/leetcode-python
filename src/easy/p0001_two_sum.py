"""
PROBLEM DESCRIPTION

Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume
that each input would have exactly one solution, and you may not use the same element twice.


EXAMPLE

- Input: nums = [2, 7, 11, 15], target = 9
- Output: [0, 1]
- Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""


from typing import List


class Solution:
  
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    numToIdxDict = {}
    
    for i in range(len(nums)):
      complement = target - nums[i]
      
      if complement not in numToIdxDict:
        numToIdxDict[nums[i]] = i
      else:
        return [numToIdxDict[complement], i]


if __name__ == '__main__':
  instance = Solution()
  print(instance.twoSum([2, 7, 11, 15], 9))
