class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix):
        snake_list = []
        for i in range(len(matrix)):
            if i % 2 == 0:
                for j in range(len(matrix[i])):
                    snake_list.append(matrix[i][j])
            else:
                for j in range(len(matrix[i])-1, -1, -1):
                    snake_list.append(matrix[i][j])
        return snake_list