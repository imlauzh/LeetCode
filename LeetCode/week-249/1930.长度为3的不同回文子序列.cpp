class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int ans=0;
        for(int i=0;i<26;++i){
            int L=0, R=s.size()-1;
            while(L<s.size() and s[L]!=i+'a')L+=1;
            while(R>0 and s[R]!=i+'a')R-=1;
            if(L>=R)continue;
            vector<int> res(26);
            for(int j=L+1;j<R;j++)res[s[j]-'a']=1;
            for(auto x : res)ans+=x;
        }
        return ans;
    }
};