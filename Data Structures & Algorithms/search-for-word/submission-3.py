class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i,j,k):
            if k == len(word):
                return True
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return False
            if board[i][j] != word[k] or board[i][j] == "#":
                return False
            temp = board[i][j]
            board[i][j] = "#"
            r1 = backtrack(i+1,j, k+1)
            r2 =backtrack(i-1,j, k+1)
            r3 =backtrack(i,j+1, k+1)
            r4 =backtrack(i,j-1, k+1)
            board[i][j] = temp
            return r1 or r2 or r3 or r4

        for i in range(m):
            for j in range(n):
                res = backtrack(i,j,0)
                if res:
                    return True
        return False
