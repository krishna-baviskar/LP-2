# Greedily picks the absolute lowest weight edge that connects two unjoined components
edges = [(1, 0, 1), (2, 1, 2), (3, 0, 2)] # (weight, u, v)
edges.sort()
visited = {edges[0][1]}

print("MST Edges:")
for w, u, v in edges:
    if (u in visited) != (v in visited): # Xor check prevents cycles for simple trees
        visited.update([u, v])
        print(f"{u} - {v} : {w}")
