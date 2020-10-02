class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        
        diff=float('inf')
        
        for k in range(len(nums)-2):
            i=k+1
            j=len(nums)-1
            while(i<j):
                currSum=nums[i]+nums[j]+nums[k]
                if(abs(target-currSum)<diff):
                    diff=abs(target-currSum)
                    v=currSum
                if(currSum==target):
                    return(currSum)
                elif(currSum<target):
                    i+=1
                else:
                    j-=1
        return(v)