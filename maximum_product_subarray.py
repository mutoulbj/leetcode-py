# -*- coding: utf-8 -*-
# maximum porduct subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6

class Solution:
    def maxProduct(self, A):
        # @param A, a list of integers
        # @return an integer
        if len(A) == 0:
            return 0
        elif len(A) == 1:
            return A[0]
        else:
            max_num = max_local = min_local = A[0]
            i = 1
            while i < len(A):
                max_copy = max_local
                max_local = max(max(max_local * A[i], A[i]), min_local * A[i])
                min_local = min(min(max_copy * A[i], A[i]), min_local * A[i])
                max_num = max(max_num, max_local)
                i += 1
            return max_num



if __name__ == '__main__':
    s = Solution()
    A = [2,3, 2, -1, 4]
    print s.maxProduct(A)

