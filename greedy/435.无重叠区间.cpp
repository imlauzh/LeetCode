/*
 * @lc app=leetcode.cn id=435 lang=cpp
 *
 * [435] 无重叠区间
 *
 * https://leetcode-cn.com/problems/non-overlapping-intervals/description/
 *
 * algorithms
 * Medium (50.44%)
 * Likes:    437
 * Dislikes: 0
 * Total Accepted:    75.6K
 * Total Submissions: 149.7K
 * Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
 *
 * 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
 * 
 * 注意:
 * 
 * 
 * 可以认为区间的终点总是大于它的起点。
 * 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: [ [1,2], [2,3], [3,4], [1,3] ]
 * 
 * 输出: 1
 * 
 * 解释: 移除 [1,3] 后，剩下的区间没有重叠。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: [ [1,2], [1,2], [1,2] ]
 * 
 * 输出: 2
 * 
 * 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: [ [1,2], [2,3] ]
 * 
 * 输出: 0
 * 
 * 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
 * 
 * 
 */

/*
 * 移除区间的最小数量, 尽量移除跨度比较大的区间
 * 可以把区间视作左闭右开区间
 * 这里只是要求移除区间个数最少, 并没有要求区间跨度要最大
 * 所以只要保证更新的过程中尽量避免因选择某个区间而导致右侧的需移除区间变多
 * 那么我们可以把问题转化成保留哪些不重合的区间
 * 首先选择一个区间作为首区间, 若下一区间与该区间有重合, 则贪心保留右端点小的区间, 即小的区间块, 直到没有任何区间与其重合时, 即确定该区间块.
 */

// @lc code=start
class Solution
{
public:
    int eraseOverlapIntervals(vector<vector<int>> &intervals)
    {
        int n = intervals.size();
        if (n < 2)
            return 0;
        // 按区间的右端点增序排序
        sort(intervals.begin(), intervals.end(), [](const auto &u, const auto &v){ return u[1] < v[1]; });

        int right = intervals[0][1];
        int ans=1;
        for(int i=1;i<n;i++){
            // 由于已经排过序了, 直接选择与前个区间不重合且右端点最小的区间即可
            if(intervals[i][0]>=right){
                ++ans;
                right=intervals[i][1];
            }
        }
        return n-ans;
    }
};
// @lc code=end
