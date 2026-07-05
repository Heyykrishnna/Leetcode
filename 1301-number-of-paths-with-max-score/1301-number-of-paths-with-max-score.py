class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)        
        dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        
        dp[n - 1][n - 1] = [0, 1]
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or board[r][c] == 'S':
                    continue

                ps = (dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                mpc = max(state[0] for state in ps)
                
                if mpc == -1:
                    continue
                    
                ways = sum(state[1] for state in ps if state[0] == mpc)
                
                if board[r][c] == 'E' :
                    val = 0
                else:
                    val = int(board[r][c])
                
                dp[r][c] = [mpc + val, ways % MOD]
                
        if dp[0][0][0] == -1:
            return [0, 0]
            
        return dp[0][0]