# Note: Dijkstra solves Single-Source Shortest Path. It is represented here on a Matrix graph setup.
V = 4
G = [[0, 4, 1, 0], [4, 0, 2, 5], [1, 2, 0, 8], [0, 5, 8, 0]]
dist, vis = [float('inf')] * V, [False] * V
dist[0] = 0

for _ in range(V):
    u = min((i for i in range(V) if not vis[i]), key=lambda x: dist[x])
    vis[u] = True
    for v in range(V):
        if G[u][v] and not vis[v]: dist[v] = min(dist[v], dist[u] + G[u][v])

print("Dijkstra Distances from 0:", dist)
