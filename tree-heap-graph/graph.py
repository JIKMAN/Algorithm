## 함수
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 전역
A, B, C, D = 0, 1, 2, 3

G = Graph(4) # 4x4 2차원 배열의 그래프
G.graph[A][B] = 1
G.graph[A][C] = 1
G.graph[A][D] = 1
G.graph[B][A] = 1
G.graph[B][C] = 1
G.graph[C][D] = 1
G.graph[C][A] = 1
G.graph[C][B] = 1
G.graph[D][A] = 1
G.graph[D][C] = 1

# Main
for i in range(4):
    for j in range(4):
        print(G.graph[i][j], end=' ')
    print()