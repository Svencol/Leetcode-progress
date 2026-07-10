class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        skip =0
        for i,letter in enumerate(s):
            if skip == 1:
                skip = 0
                continue
            if  s[i:i+2] == "IV":
                total +=4
                skip =1
            elif  s[i:i+2] == "IX":
                total +=9
                skip =1
            elif  s[i:i+2] == "XL":
                total +=40
                skip =1
            elif  s[i:i+2] == "XC":
                total +=90
                skip =1
            elif  s[i:i+2] == "CD":
                total +=400
                skip =1
            elif  s[i:i+2] == "CM":
                total +=900
                skip =1
            elif letter == "I":
                total +=1 
            elif letter == "V":
                total +=5
            elif letter == "X":
                total +=10
            elif letter == "L":
                total +=50
            elif letter == "C":
                total +=100
            elif letter == "D":
                total +=500
            elif letter == "M":
                total +=1000
        return total


            

        