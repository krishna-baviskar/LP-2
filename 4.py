N = 4
board = [["."] * N for _ in range(N)]

# Branch & Bound Trackers (Stop illegal paths instantly)
cols = [False] * N          # Checks if column has a queen
diag1 = [False] * (2 * N)   # Checks normal diagonal (\) using index: row - col
diag2 = [False] * (2 * N)   # Checks reverse diagonal (/) using index: row + col

def solve(r=0):
    if r == N:  # Base Case: All queens are successfully placed
        for row in board: print(" ".join(row))
        print(); return True # Remove "return True" to find ALL solutions
        
    for c in range(N):
        # 1. Bounding Function: Only proceed if safe
        if not cols[c] and not diag1[r - c] and not diag2[r + c]:
            
            # 2. Place Queen & Lock Paths
            board[r][c] = "Q"
            cols[c] = diag1[r - c] = diag2[r + c] = True
            
            # 3. Move to Next Row (Recursion)
            if solve(r + 1): return True 
            
            # 4. Backtrack: Undo choices if path failed
            board[r][c] = "."
            cols[c] = diag1[r - c] = diag2[r + c] = False
            
    return False

solve()
