class Solution:
    def maxScore(self, cardPoints, k):
        # write code here
        curr = sum(cardPoints[0:k])
        res = curr
        for i in range(1, k+1):
            curr += cardPoints[-i]-cardPoints[k-i]
            res = max(res, curr)
        return res
