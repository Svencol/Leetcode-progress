class Solution:
    def removeStars(self, s: str) -> str:
        curr = []
        for i,letter in enumerate(s):
            if letter != "*":
                curr.append(letter)
            else:
                curr.pop()
        return "".join(curr)