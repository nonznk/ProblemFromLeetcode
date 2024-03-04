class Solution:
    def addtwoNumbers(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        result = []
        new_l1 = ""
        new_l2 = ""

        self.l1.reverse()
        self.l2.reverse()

        for i in range(len(self.l1)):
            new_l1 = new_l1 + str(self.l1[i])
        for j in range(len(self.l2)):
            new_l2 = new_l2 + str(self.l2[j])

        new_result = int(new_l1) + int(new_l2)
        new_result_str = str(new_result)

        for k in range(len(new_result_str)):
            result_toint = new_result_str[k]
            result.append(int(result_toint))

        result.reverse()
        return result
        # print(result)


# a = Solution().addtwoNumbers([2, 4, 3], [5, 6, 4])
# a = Solution().addtwoNumbers([0], [0])
# a = Solution().addtwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
