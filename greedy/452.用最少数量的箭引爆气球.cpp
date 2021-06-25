/*
 * @lc app=leetcode.cn id=452 lang=cpp
 *
 * [452] 用最少数量的箭引爆气球
 *
 * https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
 *
 * algorithms
 * Medium (50.71%)
 * Likes:    425
 * Dislikes: 0
 * Total Accepted:    82.1K
 * Total Submissions: 161.7K
 * Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
 *
 * 
 * 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
 * 
 * 一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足
 * xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。
 * 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
 * 
 * 给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：points = [[10,16],[2,8],[1,6],[7,12]]
 * 输出：2
 * 解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
 * 
 * 示例 2：
 * 
 * 
 * 输入：points = [[1,2],[3,4],[5,6],[7,8]]
 * 输出：4
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：points = [[1,2],[2,3],[3,4],[4,5]]
 * 输出：2
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：points = [[1,2]]
 * 输出：1
 * 
 * 
 * 示例 5：
 * 
 * 
 * 输入：points = [[2,3],[2,3]]
 * 输出：1
 * 
 * Your runtime beats 59.51 % of cpp submissions
 * Your memory usage beats 45.19 % of cpp submissions (34.1 MB)
 * 
 * 与435类似, 不过策略不同
 * 要求引爆*所有*气球的最小数量
 * 那么对points两个维度先按1维升序,再按0维升序
 * 这样第一个区间的右端点就是第一支箭的位置
 * 因为再大的话, 第一个气球就不能引爆了
 * 接着把这支箭可以引爆的气球排除,
 * 剩下的区间和之前一样处理, 直到没有气球剩余
 * 
 */

// @lc code=start
class Solution
{
public:
    int findMinArrowShots(vector<vector<int>> &points)
    {
        if (points.size() < 2)
            return points.size();
        // 对points两个维度先按1维升序,再按0维升序
        sort(points.begin(), points.end(), [](const auto &u, const auto &v)
             {
                 if (u[1] == v[1])
                     return u[0] < v[0];
                 else
                     return u[1] < v[1];
             });
        vector<int> xs;
        int x = points[0][1];
        xs.push_back(x);
        for (int i = 1; i < points.size(); ++i)
        {
            // cout<<points[i][0]<<points[i][1]<<' ';
            // 之前的箭可以引爆该气球
            if (x >= points[i][0])
                continue;
            // 否则的话更新箭的位置
            else
            {
                x = points[i][1];
                xs.push_back(x);
            }
        }
        return xs.size();
    }
};
// @lc code=end
