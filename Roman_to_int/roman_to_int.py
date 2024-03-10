class Solution(object):
    def romanToInt(self, s):
        self.s = s
        val = 0
        roman_list = []
        roman_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for k in range(len(self.s)):
            print(roman_int[self.s[k]])

        for i in range(len(self.s)):
            if roman_int[self.s[i - 1]] < roman_int[self.s[i]]:
                val += roman_int[self.s[i]] - roman_int[self.s[i - 1]]

        return val


a = Solution().romanToInt("IV")
print(a)
