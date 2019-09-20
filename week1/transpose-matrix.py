class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        a = []
        newR = len(A[0])
        oldR = len(A)
        for i in range(newR):
            arr = []
            for j in range(oldR):
                arr.append(A[j][i])
            a.append(arr)
        return a