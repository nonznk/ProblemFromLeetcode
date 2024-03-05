class Solution:
    def isPalindrome(self, x):
        self.x = x
        # x_list = []
        x_str = str(self.x)
        x_new = ""

        for i in range(-1, -len(x_str) - 1, -1):
            x_new += x_str[i]
        print(x_new)

        if x_str == x_new:
            return True
        else:
            return False


a = Solution().isPalindrome(121)
print(a)
