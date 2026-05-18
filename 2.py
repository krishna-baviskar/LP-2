G = (1, 2, 3, 4, 5, 6, 7, 8, 0)
M = {0:(1,3), 1:(0,2,4), 2:(1,5), 3:(0,4,6), 4:(1,3,5,7), 5:(2,4,8), 6:(3,7), 7:(4,6,8), 8:(5,7)}

def h(s): return sum(1 for i in range(9) if s[i] and s[i] != G[i])

def P(s): [print(list(s[i:i+3])) for i in range(0, 9, 3)]; print("-" * 10)

def a_star(mat):
    S = tuple(x for r in mat for x in r)
    q, vis = [(h(S), 0, S, [S])], set()
    while q:
        q.sort()
        f, g, cur, path = q.pop(0)
        if cur == G:
            for p in path: P(p)
            return print(f"Solved in {g} moves!")
        vis.add(cur)
        i = cur.index(0)
        for n in M[i]:
            t = list(cur); t[i], t[n] = t[n], t[i]; t_t = tuple(t)
            if t_t not in vis: q.append((g + 1 + h(t_t), g + 1, t_t, path + [t_t]))

# --- Run ---
start_matrix = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
a_star(start_matrix)
