goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
moves = {0:(1,3), 1:(0,2,4), 2:(1,5), 3:(0,4,6), 4:(1,3,5,7), 5:(2,4,8), 6:(3,7), 7:(4,6,8), 8:(5,7)}

def h(s): return sum(1 for i in range(9) if s[i] and s[i] != goal[i])

def a_star(start):
    q, vis = [(h(start), 0, start)], set()
    while q:
        q.sort()
        f, g, cur = q.pop(0)
        if cur == goal: return print(f"Goal reached in {g} moves!")
        vis.add(cur)
        pos = cur.index(0)
        for nxt in moves[pos]:
            t = list(cur)
            t[pos], t[nxt] = t[nxt], t[pos]
            t_tup = tuple(t)
            if t_tup not in vis: q.append((g + 1 + h(t_tup), g + 1, t_tup))

# Run with a solvable state (0 is blank)
a_star((1, 2, 3, 4, 0, 5, 7, 8, 6))
