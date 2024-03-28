from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sortedNums = sorted(nums)
        for index, number in enumerate(sortedNums):
            if number > 0:
                break
            
            if index > 0 and number == sortedNums[index - 1]:
                continue

            left = index + 1
            right = len(sortedNums) - 1
            while left < right:
                threeSum = number + sortedNums[left] + sortedNums[right]
                if (threeSum < 0):
                    left += 1
                elif threeSum > 0:
                    right -= 1
                elif threeSum == 0:
                    result.append([number, sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1
                    while sortedNums[left] == sortedNums[left - 1] and left < right:
                        left += 1
        return result

# After copy/pasting the template from LeetCode, uncomment the following to start testing.
# solution = Solution()

