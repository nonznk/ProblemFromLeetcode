s = input("")

# new_string = ""

# for i in range(len(s)):
#     if s[i] != '"':
#         new_string = new_string + s[i]

# text_sep = new_string.split(" ")
# # print(text_sep)

# new_text = ""

# for j in range(len(text_sep)):
#     num = len(text_sep)
#     for k in range(len(text_sep[j]) - 1, -1, -1):
#         new_text = new_text + text_sep[j][k]

#     if j < num - 1:
#         new_text = new_text + " "

# new_text = '"' + new_text + '"'

# # print("Output: {}".format(new_text))
# print(new_text)


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

        # print("Output: {}".format(new_text))
        print(self.new_text)

    def __str__(self):
        return self.new_text


a = Solution()
a.reverseWords(s)
# print(a)
