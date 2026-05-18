# Format: (weight, vertex_u, vertex_v)
edges = [(1, 0, 1), (2, 1, 2), (3, 0, 2)] 

# 1. Greedy choice: Sort paths from cheapest to most expensive
edges.sort()

# 2. Start tracking connected vertices by grabbing the first node of the cheapest edge
visited = {edges[0][1]}
total_mst_weight = 0

print("--- Calculated MST ---")
# 3. Process each edge and calculate weights dynamically
for w, u, v in edges:
    # XOR check: Only pick the edge if it connects an unjoined node
    if (u in visited) != (v in visited): 
        visited.update([u, v])
        total_mst_weight += w  # Add the edge weight to the total cost
        print(f"Edge ({u} - {v}) | Weight: {w}")

print("-" * 22)
print(f"Total MST Cost = {total_mst_weight}")
