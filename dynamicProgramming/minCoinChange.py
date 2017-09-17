"""
You are given coins of different denominations "coins" and a total amount of money amount "m". 
Write a function to compute the MINIMUM number of coins you need to make "m", given the coins in "coins".
If that amount of money cannot be made up by any combination of the coins, return -1.


Axioms:
1. You have an unlimited number of each coin in coins
2. M will never be negative


Is this a combination or permutation problem?
- Combination, because 1,1,2 is the same as 2,1,1

Input:
- List coins
- Int m
- List memo

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
def make_min_coins(coins, amount, memo=None):
    #A list is faster than using a dict
    if memo is None:
        memo = [None] * (amount+1)
    
    #Read cache
    if memo[amount] !=None:
        if memo[amount] == sys.maxint:
            return -1
        else:
            return memo[amount]
    
    #Base case
    if amount in coins:
        return 1
    
    if amount <= 0:
        return 0
    
    #Backtrack
    min_coins = sys.maxint
    
    for coin in coins:
        if coin <= amount:
            candidate = 1 + make_min_coins(coins,amount-coin,memo)
            if candidate > 0:  
                min_coins = min(min_coins, candidate)

    #Write to cache
    memo[amount] = min_coins

    if min_coins == sys.maxint:
        return -1

    return min_coins

if __name__ == '__main__':
    print(make_min_coins([84,457,478,309,350,349,422,469,100,432,188], 6993))
