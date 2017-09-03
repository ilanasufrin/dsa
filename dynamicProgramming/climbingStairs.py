"""
https://leetcode.com/submissions/detail/116364238/
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can only take the number of stairs in list k. For example, if k is [1,3,5] then you can only take either 1, 3, or 5 stairs at a time.
In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs(self, n, k):
        """
        :type n: int
        :rtype: int

        #we are looking for the number of permutations

        EXAMPLE WITH k = [1,2]
        - If we are on the 0th stair, there are no ways
        - If we are on the n - 1 stair, there is 1 way: 1
        - If we are on the n - 2 stair, there are 2 ways: 1,1 or 2
        - If we are on the n - 3 stair, there are 3 ways: 1,1,1 or 2,1 or 1,2 
        - If we are on the n - 4 stair, there are 3 ways: 1,1,1,1 or 2,1,1 or 1,1,2 or 1,2,1 or 2,2

        Runtime: O(n), because we have O(N) recursive calls in the longest stack and we do O(1) work in each of them since answers are memoized
        Memory; O(n), which is derived from the memo dictionary that has a unique solution for every combo
        """
        return self.helper(n, k, {})

    """
    This helper is just a way to call climbStairs(n) with a memoization array
    """
    def helper(self, n, k, memo):
        
        #memo
        if n in memo:
            return memo[n]

        #base cases
        if n <=2:
            return n

        #backtracking
        result = 0

        for num in k:
            result += self.helper(n-num, k, memo)

        #memo
        memo[n] = result
        
        return result

s = Solution()

print(s.climbStairs(4, [1,2]))
        