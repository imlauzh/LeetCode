#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
# 暴力：长度固定，

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter # 1. 导入 Counter 类，用于方便地统计词频

        # 2. 处理边界情况：如果主字符串s或单词列表words为空，则不可能找到匹配，返回空列表
        if not s or not words:
            return []

        one_word = len(words[0]) # 3. 获取列表中第一个单词的长度，题目通常假设words中所有单词长度相同
        word_num = len(words)    # 4. 获取需要匹配的单词总数量
        n = len(s)               # 5. 主字符串s的长度
        
        # 6. 将words列表转换为Counter对象，方便查询每个目标单词的期望出现次数
        #    例如: words = ["foo", "bar", "foo"] -> words_freq = Counter({"foo": 2, "bar": 1})
        words_freq = Counter(words) 
        
        res = [] # 7. 用于存储结果，即所有满足条件的子串在s中的起始索引

        # 8. 外层循环：这个循环是解决这类问题的关键技巧之一。
        #    因为子串的起始位置可以是0, 1, ..., one_word-1 中的任意一个相对于单词长度的偏移量。
        #    例如，如果单词长度为3，一个匹配的子串可能从 s[0] 开始 (0, 3, 6...)，
        #    也可能从 s[1] 开始 (1, 4, 7...)，或从 s[2] 开始 (2, 5, 8...)。
        #    从 s[3] 开始的模式与从 s[0] 开始的模式是对齐的。
        #    所以，我们只需要检查这 one_word 种不同的起始偏移。
        for i in range(0, one_word):
            cur_cnt = 0          # 9. 当前滑动窗口中已匹配的单词数量
            left = i             # 10. 当前滑动窗口的左边界
            right = i            # 11. 当前滑动窗口的右边界（指向下一个待处理词的起始位置）
            cur_Counter = Counter() # 12. 用于统计当前滑动窗口内各个单词的出现次数

            # 13. 内层循环：滑动窗口的核心逻辑
            #     只要窗口的右边界加上一个单词的长度不超过主字符串s的长度，就继续滑动
            while right + one_word <= n:
                # 14. 从s中提取从right指针开始，长度为one_word的子串，作为当前待考察的词w
                w = s[right:right + one_word]
                right += one_word # 15. 右指针向右移动一个单词的长度，扩展窗口

                cur_Counter[w] += 1 # 16. 将提取到的词w的计数在当前窗口词频中加1
                cur_cnt += 1        # 17. 当前窗口中包含的（有效或无效）单词总数加1

                # 18. 收缩窗口的条件：
                #     如果刚加入的词w在当前窗口中的出现次数 (cur_Counter[w]) 
                #     超过了它在目标单词列表words中应该出现的次数 (words_freq[w])，
                #     或者如果w根本就不是目标单词 (此时 words_freq[w] 会是0，而 cur_Counter[w] 是1)，
                #     那么就需要从窗口左边移除单词，直到这个条件不再满足。
                while cur_Counter[w] > words_freq[w]:
                    left_w = s[left:left+one_word] # 19. 获取窗口最左边的单词
                    left += one_word               # 20. 左指针向右移动一个单词长度，收缩窗口
                    cur_Counter[left_w] -= 1       # 21. 将移除的单词left_w在当前窗口词频中减1
                    cur_cnt -= 1                   # 22. 当前窗口中包含的单词总数减1
                
                # 23. 检查是否找到了一个完整匹配：
                #     如果当前窗口中有效单词的数量 (cur_cnt) 等于目标单词列表中的单词总数 (word_num)，
                #     这意味着当前窗口 s[left:right) 可能是一个解。
                #     结合上面的收缩逻辑，能达到这个条件时，可以保证窗口内的词频与目标词频一致。
                if cur_cnt == word_num:
                    res.append(left) # 24. 将当前窗口的起始位置left添加到结果列表中
        
        return res # 25. 返回所有找到的起始索引
# @lc code=end

