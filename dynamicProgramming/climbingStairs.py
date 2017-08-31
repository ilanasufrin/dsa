"""
https://leetcode.com/submissions/detail/116364238/
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        #we are looking for the number of permutations
        - If we are on the 0th stair, there are no ways
        - If we are on the n - 1 stair, there is 1 way: 1
        - If we are on the n - 2 stair, there are 2 ways: 1,1 or 2
        - If we are on the n - 3 stair, there are 3 ways: 1,1,1 or 2,1 or 1,2 
        """
        return self.helper(n, {})

    """
    This helper function is exactly the same as climbStairs(n) but it includes a memoization array
    """
    def helper(self, n, memo):
        
        #memo
        if n in memo:
            return memo[n]

        #base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        #backtracking
        result = self.helper(n-1, memo) + self.helper(n-2, memo)

        #memo
        memo[n] = result
        
        return result
        