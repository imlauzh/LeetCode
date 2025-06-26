#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
# https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/2993894/cong-er-cha-shu-dao-er-shi-liu-cha-shu-p-xsj4

# @lc code=start
class Node:
    __slots__ = 'son', 'end'
    def __init__(self):
        self.son = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def find(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.son:
                return 0
            cur = cur.son[c]
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        return self.find(word)==2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix)!=0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

