class Solution:
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        # N students, 1 row represents 1 student 
        def find(v):
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(x, y):
            xRoot = self.find(x)
            yRoot = self.find(y)
            if xRoot == yRoot:
                return
            if xRoot > yRoot:
                parent[yRoot] = xRoot
            else:
                parent[xRoot] = yRoot
                    
        N = len(M)
        parent = [i for i in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j and M[i][j] == 1:
                    if find(i) != find(j):
                        parent[find(i)] = find(j)
        k = 0
        for i in range(len(parent)):
            if parent[i] == i:
                k += 1
        return k
                    
        