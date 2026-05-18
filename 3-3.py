# Graph dictionary: G[source] = {neighbor: weight}
G = {0: {1: 4, 2: 1}, 1: {2: 2, 3: 5}, 2: {1: 2, 3: 8}, 3: {}}

# Initialize distances: set all nodes to infinity except the source node (0)
dist = {i: float('inf') for i in G}
dist[0] = 0
unvis = set(G.keys())

while unvis:
    # Greedily pick the unvisited node with the absolute smallest calculated distance
    u = min(unvis, key=lambda x: dist[x])
    unvis.remove(u)
    
    # Update distances to all neighboring nodes
    for v, w in G[u].items():
        dist[v] = min(dist[v], dist[u] + w)

# --- Enhanced Output Formatting ---
print("--- Calculated Shortest Path Distances ---")
for node, distance in dist.items():
    print(f"Shortest distance from Node 0 to Node {node} = {distance}")
