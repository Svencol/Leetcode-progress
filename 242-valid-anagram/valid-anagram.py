class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for i in s:
            count[i] = count[i] +1

        for i in t:
            count[i] = count[i] -1
            if count[i] <0:
                return False
        if sum(count.values()) ==0:
            return True
        return False


