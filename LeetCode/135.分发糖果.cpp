/*
 * @lc app=leetcode.cn id=135 lang=cpp
 * [135] 分发糖果
 * 每个孩子至少一个
 * 评分高的也要比*两侧的孩子*更多
 * 分解成两个方向
 * 双向遍历，满足约束
 */

// @lc code=start
class Solution
{
public:
    int candy(vector<int> &r)
    {
        int size = r.size();
        if (size < 2)
            return size;
        vector<int> c(size, 1);
        for (int i = 1; i < size; i++)
        {
            if (r[i] > r[i - 1])
                c[i] = c[i - 1] + 1;
        }
        for (int i = size - 1; i > 0; i--)
        {
            if (r[i] < r[i - 1])
                c[i - 1] = max(c[i - 1], c[i] + 1);
        }
        return accumulate(c.begin(), c.end(), 0);
    }
};
// @lc code=end
