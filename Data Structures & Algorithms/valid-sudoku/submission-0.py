class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        block = defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num ==".":
                    continue
                block_i, block_j = i//3, j//3
                if num in row[i] or num in col[j] or num in block[(block_i,block_j)]:
                    return False
                else:
                    row[i].add(num)
                    col[j].add(num)
                    block[(block_i,block_j)].add(num)
        return True
                    

                