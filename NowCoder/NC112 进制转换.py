class Solution:
    def solve(self, M, N):
        # write code here
        if M == 0:
            return "0"
        s = []
        flag = True
        c = "0123456789ABCDEF"
        if M < 0:
            flag = False
            M = -M
        while M > 0:
            s.append(c[M % N])
            M = M // N
        s.reverse()
        result = "".join(s)
        return result if flag == True else "-" + result
