class Solution:
    def twoSum(self, num, target):
        self.num = num
        self.target = target

        for i in range(len(self.num)):
            for j in range(i+1, len(self.num), 1):
                if self.num[i] + self.num[j] == self.target:
                    return [i, j]