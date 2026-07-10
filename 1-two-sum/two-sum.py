class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            remaining = target - nums[i] #check if the remaining number is present in the hashMap
            if remaining in hashMap:
                return [i, hashMap[remaining]] #return if present
            hashMap[nums[i]]=i #Adding the element to the hashmap
        return []
        
        