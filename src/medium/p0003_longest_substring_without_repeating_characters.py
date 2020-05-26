"""
PROBLEM DESCRIPTION

Given a string, find the length of the longest substring without repeating characters.


EXAMPLE 1

- Input: "abcabcbb"
- Output: 3
- Explanation: The answer is "abc", with the length of 3.


EXAMPLE 2

- Input: "bbbbb"
- Output: 1
- Explanation: The answer is "b", with the length of 1.


EXAMPLE 3

- Input: "pwwkew"
- Output: 3
- Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
  subsequence and not a substring.
"""


class Solution:
  
  def lengthOfLongestSubstring(self, s: str) -> int:
    startIdx = 0 # Inclusive
    endIdx = 0 # Inclusive
    currCount = 0
    maxCount = 0
    charToIdxDict = {}
    
    while endIdx < len(s):
      currChar = s[endIdx]
      
      if currChar in charToIdxDict: # If currChar appeared before
        # If the previous occurrence is before startIdx, then do not move startIdx.
        # If the previous occurrence is at or after startIdx, then move startIdx after the index of previous occurrence.
        # In this way, there's no need to remove from charToIdxDict.
        startIdx = max(startIdx, charToIdxDict[currChar] + 1)
      
      currCount = endIdx - startIdx + 1
      maxCount = currCount if currCount > maxCount else maxCount
      charToIdxDict[currChar] = endIdx
      
      # Update variable to prepare for next loop iteration.
      endIdx += 1
    
    return maxCount

if __name__ == '__main__':
  instance = Solution()
  print(instance.lengthOfLongestSubstring("abcabcbb"))
