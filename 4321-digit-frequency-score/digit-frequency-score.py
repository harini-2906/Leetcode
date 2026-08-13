class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        count=[0]*10
        while n>0:
            count[n%10]+=1
            n//=10
        ans=0
        for d in range(10):
            ans+=d*count[d]
        return ans