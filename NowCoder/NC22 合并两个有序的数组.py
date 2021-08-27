#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
class Solution:
    def merge(self, A, m, B, n):
        # write code here
        pos = m+n-1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if A[m] >= B[n]:
                A[pos] = A[m]
                m -= 1
                pos -= 1
            else:
                A[pos] = B[n]
                n -= 1
                pos -= 1
        while n >= 0:
            A[pos] = B[n]
            n -= 1
            pos -= 1
        return A
