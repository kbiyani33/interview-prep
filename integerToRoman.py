class Solution:
    def intToRoman(self, num: int) -> str:
        hashTable = [
            (1000,"M"), 
            (900, "CM"), 
            (500, "D"), 
            (400, "CD"), 
            (100, "C"), 
            (90, "XC"),
            (50, "L"), 
            (40, "XL"), 
            (10, "X"), 
            (9, "IX"), 
            (5, "V"), 
            (4, "IV"), 
            (1, "I")
        ]
        result = []
        for val,symbol in hashTable:
            q = num//val
            if q>0:
                result += q*[symbol]
            num = num%val
        return "".join(result)