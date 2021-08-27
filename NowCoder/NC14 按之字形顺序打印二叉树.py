# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 两个栈轮流进栈和出栈, 加入res的顺序不一致
# 一个先加左,另一个先加右
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        s1,s2=[],[]
        res=[]
        s1.append(pRoot)
        while s1 or s2:
            if s1:
                tmp=[]
                while s1:
                    tmpRoot=s1.pop()
                    tmp.append(tmpRoot.val)
                    if tmpRoot.left:
                        s2.append(tmpRoot.left)
                    if tmpRoot.right:
                        s2.append(tmpRoot.right)
                res.append(tmp)
            if s2:
                tmp=[]
                while s2:
                    tmpRoot=s2.pop()
                    tmp.append(tmpRoot.val)
                    if tmpRoot.right:
                        s1.append(tmpRoot.right)
                    if tmpRoot.left:
                        s1.append(tmpRoot.left)
                res.append(tmp)
        return res