/*
 * @lc app=leetcode.cn id=455 lang=cpp
 * [455] 分发饼干
 * 目标是尽可能满足越多数量的孩子
 * 所以首先最容易吃饱的孩子，也就是g[i]最小的
 * 其次针对每个孩子寻找刚好能够满足他的饼干
 * 具体：把两个数组从小到大排序，按顺序分配
 */

// @lc code=start
class Solution
{
public:
    int findContentChildren(vector<int> &g, vector<int> &s)
    {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int k = 0;
        int c = 0;
        while (k < g.size() && c < s.size())
        {
            if (s[c] >= g[k])
                ++k;
            ++c;
        }
        return k;
    }
};
// @lc code=end
