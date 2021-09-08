n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

def solution(n, s, a, b, fares):
    vertex = [[40000000 for _ in range(n+ 1)] for _ in range(n+ 1)]

    for i in range(1, n+1):
        vertex[i][i] = 0

    for fare in fares:
        vertex[fare[0]][fare[1]] = fare[2]
        vertex[fare[1]][fare[0]] = fare[2]


    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                vertex[i][j] = min(vertex[i][j], vertex[i][k] + vertex[k][j])

    result = min([vertex[s][i]+vertex[i][a]+vertex[i][b] for i in range(1, n+1)])

    return result