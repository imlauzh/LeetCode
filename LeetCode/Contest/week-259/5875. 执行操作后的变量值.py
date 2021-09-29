class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res=0
        for op in operations:
            if '--' in op:
                res-=1
            elif '++' in op:
                res+=1
        return res