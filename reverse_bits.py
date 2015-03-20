class Solution:
    # @param n, an integer
    # @return, an integer
    def reverseBits(self, n):
        n_bin = bin(n)[-1: 1: -1] # remove '0b' of the bin string and reverse it
        n_reversed = n_bin + (32 - len(n_bin)) * '0' # append 0 if not 32 bit
        return int(n_reversed, base=2)

if __name__ == '__main__':
    s = Solution()
    print s.reverseBits(43261596)
