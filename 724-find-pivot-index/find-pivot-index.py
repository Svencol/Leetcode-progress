class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tt = sum(nums)
        currenttotal = 0
        for i,number in enumerate(nums):
            tt = tt - number
            if currenttotal == tt:
                return i
            currenttotal = currenttotal + number
        return -1