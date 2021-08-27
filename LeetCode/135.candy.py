#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (35.32%)
# Likes:    2037
# Dislikes: 219
# Total Accepted:    181.8K
# Total Submissions: 514.6K
# Testcase Example:  '[1,0,2]'
#
# There are n children standing in a line. Each child is assigned a rating
# value given in the integer array ratings.
# 
# You are giving candies to these children subjected to the following
# requirements:
# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 
# Return the minimum number of candies you need to have to distribute the
# candies to the children.
# 
# 
# Example 1:
# 
# 
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
# 
# 
# Example 2:
# 
# 
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two
# conditions.
# 
# 
# 
# Constraints:
# 
# 
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def candy(self, r: List[int]) -> int:
        n=len(r)
        ret=[1]*n
        for i in range(1,n):
            if r[i]>r[i-1]:
                ret[i]=max(ret[i],ret[i-1]+1)
        for i in range(n-2,-1,-1):
            if r[i]>r[i+1]:
                ret[i]=max(ret[i],ret[i+1]+1)
        return sum(ret)
# @lc code=end

