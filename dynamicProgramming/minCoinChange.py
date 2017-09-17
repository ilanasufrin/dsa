"""
You are given coins of different denominations "coins" and a total amount of money amount "m". 
Write a function to compute the MINIMUM number of coins you need to make "m", given the coins in "coins"


Axioms:
1. You have an unlimited number of each coin in coins
2. M will never be negative


Is this a combination or permutation problem?
- Combination, because 1,1,2 is the same as 2,1,1

Input:
- List coins
- Int m
- Dict memo

Return:
- Int minCoins

Runtime with cache: 
How many levels? m * len(coins)
How much work at each level? m
len(coins) * m^2

Space with cache:
The size of the cache, or m*len(coins)

"""
import sys
def min_change(coins, m, memo={}):
    #Read from the cache
    if m in memo:
        return memo[m]
    
    #Base cases
    if m in coins:
        return 1

    #Backtracking
    minCoins = sys.maxint

    for coin in coins:
        if coin <= m:
            minCoins = min(minCoins, 1+min_change(coins,m-coin, memo))

    #Populate the cache
    memo[m] = minCoins

    return minCoins

if __name__ == '__main__':
    print(min_change([1,5,10,25], 63, {}))

