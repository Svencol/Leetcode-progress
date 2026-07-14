class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = Counter(nums)
        max_key = max(l, key=l.get)
        return max_key