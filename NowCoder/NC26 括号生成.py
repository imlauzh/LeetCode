#
# 
# @param n int整型 
# @return string字符串一维数组
#
class Solution:
    def generateParenthesis(self , n ):
        # write code here
        def dfsParenthesis(str,left,right):
            # 两个都不剩下，就可以加入res
            if left==0 and right==0:
                self.res.append(str)
                return
            # 两边相等，此时只能加入左括号
            if left==right:
                dfsParenthesis(str+'(',left-1,right)
            elif left<right:
                # 因为左括号的剩余数量小于等于右括号
                # 所以需要判断一下此时是否还可以加入左括号
                if left>0:
                    dfsParenthesis(str+'(',left-1,right)
                dfsParenthesis(str+')',left,right-1)
        if n<=0:
            return []
        self.res=[]
        dfsParenthesis("",n,n)
        return self.res