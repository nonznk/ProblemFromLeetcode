class Solution:
    def addtwoNumbers(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

        new_l1 = ''
        new_l2 = ''
        result = []
        
        for i in range(-1, -len(self.l1)-1, -1):
            new_l1 = new_l1 + str(self.l1[i])
        for j in range(-1, -len(self.l2)-1, -1):
            new_l2 = new_l2 + str(self.l2[j])

        val = int(new_l1) + int(new_l2)

        for k in range(-1, -len(str(val))-1, -1):
            result.append(int(str(val)[k]))

        # print(result)

# a = Solution().addtwoNumbers([2, 4, 3], [5, 6, 4])