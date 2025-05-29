#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
# 关键是气球的结束坐标正序排序，第一个结束坐标就是第一支弓箭的位置
# 一支箭需要尽可能多引爆气球，那么需要尽可能向右移动，最远的位置也就是结束坐标中最小的点
# 确定了每支箭的位置后，接下来判断每支箭能引爆多少气球，全部都引爆完成后，就是最少的弓箭

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # 如果气球列表为空，则不需要箭。
        if not points:
            return 0

        # 1. 贪心策略的关键：将气球按照结束坐标 (x_end) 进行升序排序。
        #    如果结束坐标相同，次要排序依据（例如起始坐标）对这个特定贪心策略的正确性没有严格影响。
        points.sort(key=lambda x: x[1])

        # 2. 初始化所需箭的数量。
        #    对于排序后的第一个气球，我们至少需要一支箭。
        arrows_needed = 1
        
        #    记录第一支（也是当前最新一支）箭的射出位置的 x 坐标。
        #    我们选择射在第一个气球的结束坐标点，这样可以确保第一个气球被射爆，
        #    并且这支箭能尽可能地延伸，有机会射爆后续的气球。
        arrow_shot_at_x = points[0][1]

        # 3. 从第二个气球开始遍历排序后的气球列表。
        for i in range(1, len(points)):
            current_balloon_start = points[i][0]  # 当前气球的开始坐标
            current_balloon_end = points[i][1]    # 当前气球的结束坐标

            # 检查当前气球的开始坐标是否大于上一支箭的射出位置。
            # 如果大于，说明上一支箭无法覆盖到当前这个气球。
            if current_balloon_start > arrow_shot_at_x:
                # 因此，我们需要一支新的箭。
                arrows_needed += 1
                # 更新箭的射出位置为当前气球的结束坐标。
                # 这样做是为了确保当前气球被射爆，并且这支新箭能尽可能向右延伸。
                arrow_shot_at_x = current_balloon_end
            # else (current_balloon_start <= arrow_shot_at_x):
            #   如果当前气球的开始坐标不大于上一支箭的射出位置，
            #   意味着当前气球可以被之前在 arrow_shot_at_x 位置射出的箭所引爆。
            #   （因为箭在 x 点射出，能引爆 [start, end] 的气球条件是 start <= x <= end。
            #    我们已知 current_balloon_start <= arrow_shot_at_x。
            #    同时，arrow_shot_at_x 是某个（可能是更早的）气球的 end 坐标。
            #    由于已经按 end 坐标排序，当前气球的 end 坐标必然大于等于定义了 arrow_shot_at_x 的那个气球的 end 坐标，
            #    所以 arrow_shot_at_x <= current_balloon_end 也能保证，从而当前气球被覆盖。）
            #   因此，不需要新的箭，并且 arrow_shot_at_x 的位置保持不变，
            #   因为它代表了上一支箭的有效射击点。

        # 返回所需的最少箭数。
        return arrows_needed
# @lc code=end

