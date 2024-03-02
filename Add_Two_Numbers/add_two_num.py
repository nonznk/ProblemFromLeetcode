class Solution:
    def addtwoNumbers(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        result = []

        self.l1.reverse()
        self.l2.reverse()
        
        for i, j in zip(self.l1, self.l2):
            result.append(i + j) # [7, 10, 7]

        for k in range(len(result)):
            if result[k] >= 10:
                result[k] = result[k] - 10
                result[k-1] = result[k-1] + 1
        
        result.reverse()

        # print(result)

# a = Solution().addtwoNumbers([2, 4, 3], [5, 6, 4])