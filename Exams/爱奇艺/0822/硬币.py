#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def change(self, amount, coins):
        # Write Code Here
        dp = [0]*(amount+1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount+1):
                dp[i]+=dp[i-c]
        return dp[amount]

_amount = int(input())

_coins_cnt = 0
_coins_cnt = int(input())
_coins_i = 0
_coins = []
while _coins_i < _coins_cnt:
    _coins_item = int(input())
    _coins.append(_coins_item)
    _coins_i += 1


s = Solution()
res = s.change(_amount, _coins)

print(str(res) + "\n")
