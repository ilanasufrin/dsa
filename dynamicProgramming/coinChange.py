"""
You are given coins of different denominations "coins" and a total amount of money amount "m". 
Write a function to compute how many ways you can make "m" with the coins in "coins"


Axioms:
1. You have an unlimited number of each coin in coins
2. M will never be negative


Is this a combination or permutation problem?
- Combination, because 1,1,2 is the same as 2,1,1

Input:
- List coins
- Int m

Return:
- Int m

Runtime: 
How many levels? m * len(coins) 
How much work are we doing at each level? m
len(coins) * m^2

Space:
The size of the cache, or m*len(coins)
"""
def make_change(coins, m, memo={}):
    #Read from the cache
    #We are going to cache our result by m and the length of coins
    if m in memo and len(coins) in memo[m]:
        return memo[m][len(coins)]

    # Base cases
    if m == 0:
        return 1
    if m < 0:
        return 0
    if len(coins) < 1: #there are no coins left to consider
        return 0;

    #Backtracking
    num_ways = 0
    num_curr_coin = 0
    current_total = 0

    # we are always currently working on the first coin in the array
    while (current_total <= m):
        num_ways += make_change(coins[1:], m-current_total, memo)
        num_curr_coin +=1
        current_total = coins[0] * num_curr_coin

    #Populate the cache
    if m not in memo:
        memo[m] = {}
    memo[m][len(coins)] = num_ways

    return num_ways

if __name__ == '__main__':
    print(make_change([1,2,3], 4, {}))