class Solution:
    def leaders(self, A, N):
        result = []
        max_right = A[N-1]
        result.append(max_right)
        
        for i in range(N-2,-1,-1):
            if A[i] >= max_right:
                result.append(A[i])
                max_right = A[i]      
        result.reverse()  
        return result