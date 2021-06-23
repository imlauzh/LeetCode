/*
 * @lc app=leetcode.cn id=5789 lang=cpp
 *
 * [5789] 你完成的完整对局数
 * 调整开始的分钟数, 使他位于完整对局的开始
 */

// @lc code=start
#include <bits/stdc++.h>
class Solution
{
public:
    int numberOfRounds(string st, string ft)
    {
        int s=60*stoi(st.substr(0, 2))+stoi(st.substr(3, 2));
        int f=60*stoi(ft.substr(0, 2))+stoi(ft.substr(3, 2));
        if(f<s)f+=1440;
        f=f/15*15;
        return max(0,(f-s))/15;
    }
};
// @lc code=end
