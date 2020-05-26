"""
PROBLEM DESCRIPTION

Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is
divisible by three.


EXAMPLE 1

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).


EXAMPLE 2

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.


EXAMPLE 3

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).


CONSTRAINTS

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""


from typing import List
from sortedcontainers import SortedList


class Solution:
  
  def maxSumDivThree(self, nums: List[int]) -> int:
    remainderToNumsDict = {0: SortedList(), 1: SortedList(), 2: SortedList()}
    for num in nums:
      remainder = num % 3
      if remainder == 1:
        remainderToNumsDict[1].add(num)
      elif remainder == 2:
        remainderToNumsDict[2].add(num)
    
    total = sum(nums)
    
    if total % 3 == 0:
      return total
    elif total % 3 == 1:
      ans0 = total - remainderToNumsDict[1][0] if len(remainderToNumsDict[1]) >= 1 else 0
      ans1 = total - remainderToNumsDict[2][0] - remainderToNumsDict[2][1] if len(remainderToNumsDict[2]) >= 2 else 0
      return max(ans0, ans1)
    elif total % 3 == 2:
      ans0 = total - remainderToNumsDict[2][0] if len(remainderToNumsDict[2]) >= 1 else 0
      ans1 = total - remainderToNumsDict[1][0] - remainderToNumsDict[1][1] if len(remainderToNumsDict[1]) >= 2 else 0
      return max(ans0, ans1)


if __name__ == '__main__':
  instance = Solution()
  print(instance.maxSumDivThree([3, 6, 5, 1, 8]))
