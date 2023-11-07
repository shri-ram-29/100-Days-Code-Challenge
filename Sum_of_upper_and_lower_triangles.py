class Solution:
    def sumTriangles(self, matrix, n):
        upper_sum = 0
        lower_sum = 0

        for i in range(n):
            for j in range(i, n):
                upper_sum += matrix[i][j]

        for i in range(n):
            for j in range(i + 1):
                lower_sum += matrix[i][j]
        
        return [upper_sum, lower_sum]