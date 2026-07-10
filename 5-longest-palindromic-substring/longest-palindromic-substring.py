class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStr = ""
        for i,letter in enumerate(s):
            left = i
            right = i+1
            while left >= 0 and right <len(s) and s[left] == s[right]:
                currentStr = s[left:right+ 1]
                if len(currentStr) > len(maxStr):
                    maxStr = currentStr
                left -= 1
                right +=1
            left = i
            right = i+2
            while left >= 0 and right <len(s) and s[left] == s[right]:
                currentStr = s[left:right + 1]
                if len(currentStr) > len(maxStr):
                    maxStr = currentStr
                left -= 1
                right +=1
            if len(maxStr) == 0:
                maxStr = letter

        return maxStr


                

            
