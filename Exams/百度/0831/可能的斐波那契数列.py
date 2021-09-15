# 可能的斐波那契数列
class Fibonacci:
    def splitIntoFibonacci(self, num: str):
        def backTrack(index):
            if index==len(num):
                if len(seq)>2:
                    res.append(seq[:])
                    return True
                return False
            curr=0
            for i in range(index,len(num)):
                if i>index and num[index]=='0':
                    break
                curr=curr*10+ord(num[i])-ord('0')
                if len(seq)>2 and curr<seq[-1]:
                    continue
                if curr>2**31-1:
                    break
                if len(seq)<2 or curr==seq[-2]+seq[-1]:
                    seq.append(curr)
                    if backTrack(i+1):
                        return True
                    seq.pop()
                elif len(seq)>=2 and curr>seq[-2]+seq[-1]:
                    break
            return False
        res=[]
        seq=[]
        backTrack(0)
        return res


if __name__ == '__main__':
    fib = Fibonacci()
    nums = '1123581321'
    res = fib.splitIntoFibonacci(nums)
    print(res)
