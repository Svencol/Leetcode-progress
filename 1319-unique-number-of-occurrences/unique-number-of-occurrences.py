class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = Counter(arr)
        count = []
        for i in occur:
            if occur[i] not in count:
                count.append(occur[i])
            else:
                return False
        return True

        