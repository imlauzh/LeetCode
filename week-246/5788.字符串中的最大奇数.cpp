/*
 * @lc app=leetcode.cn id=5788 lang=cpp
 * [5788] 字符串中的最大奇数
 * 贪心找到最后一个奇数即可
 */

// @lc code=start
class Solution {
public:
    string largestOddNumber(string num) {
        int idx=-1;
        for(int i=0;i<num.length();i++){
            if((num[i]-'0')%2!=0)idx=i;
        }
        if(idx==-1)return "";
        else return num.substr(0,idx+1);
    }
};
// @lc code=end

