class Solution:
    count = defaultdict[int]
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        t = Counter(nums1)
        s = Counter(nums2)
        list1 =[]
        list2 = []
        for i in nums1:
            if i not in s and i not in list1:
                list1.append(i)
        for i in nums2:
            if i not in t and i not in list2:
                list2.append(i)
        return [list1,list2]
                



