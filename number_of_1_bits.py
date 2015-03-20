class Solution:
    def hammingWeight(self, n):
        n_bin = bin(n)
        count = 0
        for i in n_bin[1:]:
            if i == '1':
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print s.hammingWeight(11)
