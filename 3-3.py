# Finds shortest paths from a single source node to all other nodes
G = {0: {1: 4, 2: 1}, 1: {2: 2, 3: 5}, 2: {1: 2, 3: 8}, 3: {}}
dist = {i: float('inf') for i in G}
dist[0] = 0
unvis = set(G.keys())

while unvis:
    u = min(unvis, key=lambda x: dist[x])
    unvis.remove(u)
    for v, w in G[u].items():
        dist[v] = min(dist[v], dist[u] + w)

print("Shortest Paths from 0:", dist)
