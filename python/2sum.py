class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d=defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        
        nums.sort()
        i=0
        j=len(nums)-1
        while(i<j):
            if(nums[i]+nums[j]==target):
                return([d[nums[i]][0],d[nums[j]][-1]])
            elif(nums[i]+nums[j]<target):
                i+=1
            else:
                j-=1
        
        
        