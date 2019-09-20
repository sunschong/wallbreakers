class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i].reverse()
            A[i] = [1 - A[i][j] for j in range(len(A[i]))]
        return A