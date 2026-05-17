# Undirected Graph represented as an Adjacency List
G = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1], 4: [1, 2]}

# Iterative BFS
def bfs(start):
    vis, q = {start}, [start]
    while q:
        curr = q.pop(0)
        print(curr, end=" ")
        q.extend([n for n in G[curr] if n not in vis and not vis.add(n)])

# Recursive DFS 
def dfs(curr, vis=set()):
    if curr not in vis:
        print(curr, end=" ")
        vis.add(curr)
        for n in G[curr]: dfs(n, vis)

# --- Execution ---
print("BFS:"); bfs(0)
print("\nDFS:"); dfs(0)
