# https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(size):
            for j in range((size - 1) // 2 + 1):
                matrix[i][j], matrix[i][size - j - 1] = matrix[i][size - j - 1], matrix[i][j]
            
        