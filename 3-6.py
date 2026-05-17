edges = [(10, 0, 1), (6, 0, 2), (5, 0, 3), (15, 1, 3), (4, 2, 3)] # (w, u, v)
edges.sort()
parent = list(range(4))

def find(i): return i if parent[i] == i else find(parent[i])

print("Kruskal's MST Edges:")
for w, u, v in edges:
    root_u, root_v = find(u), find(v)
    if root_u != root_v:
        parent[root_u] = root_v
        print(f"{u} - {v} : {w}")
