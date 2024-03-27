# Copy/paste template from LeetCode below
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given nums = [-1, 0, 1, 2, -1, -4], find triplets that sum up to 0.
        The triplets cannot contain duplicates of the same element, but if there
        multiple elements with the same value that is okay.
        output: [[-1, -1, 2], [-1, 0, 1]]

        Although this is a good two pointer problem, this solution uses sets instead.
        Organize nums into three different vectors– by zero values , negative numbers, and
        positive numbers.

        Create a negative set and a positive set from the vectors of negative and
        positive numbers. Given a pair, we will look in these sets to find a value
        to form triplets that sum to 0. Because these triplets cannot contain duplicates,
        we need our sets to not contain duplicates. Since we're doing a lookup, sets are
        great for a O(1) lookup time.
        Explanation:
        nums = [-1, -2, 0, 3, 4, 3]
        pos = [3, 4, 3]
        neg = [-1, -2]
        zero = [0]
        posSet = {3, 4, 3} # sets can't contain duplicates, but for example lets imagine they do
        negSet = {-1, -2}
        Given the pair (-1, -2), we need to find 3 in the positive set to sum to 0. If positive set
        had two 3s, the two possible triplets we can have are: (-1, -2, 3) and (-1, -2, 3), which
        are duplicate triplets and will produce an incorrect output. Hence we don't want duplicates
        in the set where we are looking for complementary values.

        We do not make a set for our zero values.

        Begin logic:
        The easiest set of triplets that sum to 0 is a triplet of all 0s (0,0,0).
        If our zero list has >= at least 3 zeroes, add a (0, 0, 0) to our results.

        If we have at least one 0, we can easily form a triplet for every number and
        its negative counterpart. That is, (-1, 0, 1), (-2, 0 ,2), (-3, 0, 3)...
        We can easily do this by:
        Check if we have atleast one 0, then for every positive number, look for -1 * number
        in the negative set. If that negative counterpart exists, add (-1 * number, 0, number)
        triplet to our result.

        Now we look for pairs of negative numbers.
        We look through out negative VECTOR (not our negative set), to form every possible pair
        of negative numbers. For our sample input, those possible pairs are (-1, -1) and (-1, -4).
        Then we look for the complementary positive value inside of the positive SET. If it exists in
        the positive set, we have a complete triplet!

        We do the same thing when looking through pairs of positive values, and finding
        the completmentary negative number.
        
        Although this solution beats 92% of the other submissions, its time complexity is O(n^2) for
        forming pairs throughout the negative vector with a nested for loop.
        In the worst case, nums could contain only negative numbers, and forming pairs will be a 
        O(n^2) endeavor. This is the same for forming positive pairs if nums contains only positive numbers.
        
        The space complexity is O(n) for creating sets and vectors, with n being the number of elements
        in our input vector.
        """
        result = set()
        neg = [number for number in nums if number < 0]
        pos = [number for number in nums if number > 0]
        zero = [number for number in nums if number == 0]
        negSet = set(neg)
        posSet = set(pos)
        
        if len(zero) >= 3:
            result.add((0,0,0))

        if zero:
            for number in posSet:
                if -1 * number in negSet:
                    result.add((-1 * number, 0, number))
        
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                target = -1 * (neg[i] + neg[j])
                if target in posSet:
                    result.add(tuple(sorted([neg[i], neg[j], target])))

        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                target = -1 * (pos[i] + pos[j])
                if target in negSet:
                    result.add(tuple(sorted([target, pos[i], pos[j]])))
        
        return result

# After copy/pasting the template from LeetCode, uncomment the following to start testing.
# solution = Solution()

