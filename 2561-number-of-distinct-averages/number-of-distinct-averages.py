class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        result=[]
        for i in range (len(nums)//2):
            min1=min(nums)
            max1=max(nums)
            av=(min1+max1)/2
            result.append(av)
            nums.remove(min1)
            nums.remove(max1)
        return len(list(set(result)))    

        