s = input("")


class Solution:
    # def __init__(self, s):
    #     self.s = s

    def reverseWords(self, s):
        self.s = s
        self.new_string = ""
        self.new_text = ""

        for i in range(len(self.s)):
            if self.s[i] != '"':
                self.new_string = self.new_string + self.s[i]

        text_sep = self.new_string.split(" ")
        # print(text_sep)

        for j in range(len(text_sep)):
            num = len(text_sep)
            for k in range(len(text_sep[j]) - 1, -1, -1):
                self.new_text = self.new_text + text_sep[j][k]

            if j < num - 1:
                self.new_text = self.new_text + " "

        self.new_text = '"' + self.new_text + '"'
        return self.new_text

    def __str__(self):
        return self.new_text


Solution().reverseWords(s)
# a.reverseWords(s)
# print(a)
