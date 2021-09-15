class Solution:
    def softmax(self, logits, k):
        def e(logits):
            import math
            for i in range(k):
                logits[i]=math.exp(logits[i])
        e(logits)
        s = sum(logits)
        max = float('-inf')
        maxIdx = -1
        for i in range(k):
            if logits[i] > max:
                max = logits[i]
                maxIdx = i
        print(maxIdx, format(max/s, '.6f'))

if __name__ == "__main__":
    import sys
    numbers = str(sys.stdin.readline().strip())
    values = list(map(int, numbers.split(' ')))
    s = Solution()
    for i in range(values[0]):
        logits = str(sys.stdin.readline().strip())
        logits = list(map(float, logits.split(' ')))
        s.softmax(logits, values[1])