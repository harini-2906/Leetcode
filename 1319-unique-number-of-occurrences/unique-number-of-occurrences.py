class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        s=set()
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for val in freq.values():
            if val in s:
                return False
            s.add(val)
        return True            

    
        