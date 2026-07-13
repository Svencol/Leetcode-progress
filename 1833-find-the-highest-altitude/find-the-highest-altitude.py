class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxTotal = 0
        currentTotal = 0
        for i in gain:
            currentTotal = currentTotal+ i
            maxTotal = max(currentTotal,maxTotal)
        return maxTotal