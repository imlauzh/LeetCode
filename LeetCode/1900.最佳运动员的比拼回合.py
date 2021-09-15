#
# @lc app=leetcode.cn id=1900 lang=python3
#
# [1900] 最佳运动员的比拼回合
#
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # players：比赛队员，winner：获胜队员，player1, player2：进行比赛的双方
        # round：比赛轮次
        def dfs(players, winner, player1, player2, round):
            # 轮空
            if player1 == player2:
                dfs(players, winner+[players[player1]],
                    player1+1, player2-1, round)
                return
            # 一轮完成，进行下一轮
            elif player1 > player2:
                dfs(sorted(winner), [], 0, len(winner)-1, round+1)
                return
            # 两强相遇，更新res
            if (players[player1] == firstPlayer and players[player2] == secondPlayer) or (players[player2] == firstPlayer and players[player1] == secondPlayer):
                res[0] = min(res[0], round)
                res[1] = max(res[1], round)
            # 碾压
            elif players[player1] == firstPlayer or players[player1] == secondPlayer:
                dfs(players, winner+[players[player1]],
                    player1+1, player2-1, round)
            elif players[player2] == firstPlayer or players[player2] == secondPlayer:
                dfs(players, winner+[players[player2]],
                    player1+1, player2-1, round)
            # 其余都可能获胜，两个分支都走
            else:
                dfs(players, winner+[players[player1]],
                    player1+1, player2-1, round)
                dfs(players, winner+[players[player2]],
                    player1+1, player2-1, round)
            return
        res = [float('inf'), float('-inf')]
        dfs([i+1 for i in range(n)], [], 0, n-1, 1)
        return res
    
    
# @lc code=start
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # players：比赛队员，winner：获胜队员，player1, player2：进行比赛的双方
        # round：比赛轮次
        def dfs(players, winner, player1, player2, round):
            # 轮空
            if player1 == player2:
                dfs(players, winner+[players[player1]],
                    player1+1, player2-1, round)
                return
            # 一轮完成，进行下一轮
            elif player1 > player2:
                dfs(sorted(winner), [], 0, len(winner)-1, round+1)
                return
            # 两强相遇，更新res
            if (players[player1] == firstPlayer and players[player2] == secondPlayer) or (players[player2] == firstPlayer and players[player1] == secondPlayer):
                res[0] = min(res[0], round)
                res[1] = max(res[1], round)
            # 碾压
            elif players[player1] == firstPlayer or players[player1] == secondPlayer:
                dfs(players, winner+[players[player1]],
                    player1+1, player2-1, round)
            elif players[player2] == firstPlayer or players[player2] == secondPlayer:
                dfs(players, winner+[players[player2]],
                    player1+1, player2-1, round)
            # 其余都可能获胜，两个分支都走
            else:
                dfs(players, winner+[players[player1]],
                    player1+1, player2-1, round)
                dfs(players, winner+[players[player2]],
                    player1+1, player2-1, round)
            return
        res = [float('inf'), float('-inf')]
        dfs([i+1 for i in range(n)], [], 0, n-1, 1)
        return res
# @lc code=end
