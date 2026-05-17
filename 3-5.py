INF, V = 999, 5
G = [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]
vis = [False] * V
vis[0] = True

print("Prim's MST Edges:")
for _ in range(V - 1):
    m, x, y = INF, 0, 0
    for i in range(V):
        if vis[i]:
            for j in range(V):
                if not vis[j] and G[i][j] and m > G[i][j]: m, x, y = G[i][j], i, j
    print(f"{x} - {y} : {m}")
    vis[y] = True
