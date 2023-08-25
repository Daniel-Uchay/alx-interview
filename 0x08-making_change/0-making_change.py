#!/usr/bin/python3
'''
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount total.
'''
import sys

def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0
    
    coin_count = [sys.maxsize] * (total + 1)
    coin_count[0] = 0
    
    num_coins = len(coins)
    for i in range(1, total + 1):
        for j in range(num_coins):
            if coins[j] <= i:
                sub_coin_count = coin_count[i - coins[j]]
                if sub_coin_count != sys.maxsize:
                    coin_count[i] = min(coin_count[i], sub_coin_count + 1)
    
    if coin_count[total] == sys.maxsize:
        return -1
    
    return coin_count[total]
