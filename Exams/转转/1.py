class TopK:
    def getK(self,nums,k):
        def partition(left,right):
            pivot=left+(right-left)//2
            nums[right],nums[pivot]=nums[pivot],nums[right]
            idx=left
            for i in range(left,right):
                if nums[i]>nums[right]:
                    nums[i],nums[idx]=nums[idx],nums[i]
                    idx+=1
            nums[right],nums[idx]=nums[idx],nums[right]
            return idx
        def qselect(left,right):
            if left>=right:
                return
            mid=partition(left,right)
            if mid==k-1:
                return
            elif mid<k-1:
                qselect(mid+1,right)
            else:
                qselect(left,mid-1)
        qselect(0,len(nums)-1)
        return nums[k-1]


tk=TopK()
nums=[1,2,3,4,5,6,7,8,9,10]
k=2
res=tk.getK(nums,k)
print(res)
