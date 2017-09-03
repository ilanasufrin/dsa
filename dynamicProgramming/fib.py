"""
DP practice using a dictionary to memoize a solution
"""
class Fib:
    """
    Start of the fibonacci sequence, for sanity check: 1,1,2,3,5,8,13,21

    Memory complexity: O(n), which comes from the dictionary used to hold a unique value answer for each key value of n
    Runtime complexity: O(n) because we're doing that many recursive calls and O(1) work in each call - TODO clear with @DanielHabib
    """
    def calc_fib(self, n, memo):
        if memo is None:
            memo = {}

        # First consult our memoization dict to see if the answer is already in there
        if n in memo:
            return memo[n]

        #Base cases- how do we know when to return from the recursion?
        if n <= 0:
            return 0
        if n == 1:
            return 1

        #Here are the overlapping subproblems which will give us our answer (backtracking)
        #Also populate the memo so we can leverage this answer in the future
        memo[n] = self.calc_fib(n-1, memo) + self.calc_fib(n-2, memo)

        return memo[n]


f = Fib()

result = f.calc_fib(5, {})

print(result)
