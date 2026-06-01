class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = defaultdict(set)
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell.isdigit():
                    if cell in hashmap[("row", row)]:
                        return False
                    hashmap[("row", row)].add(cell)
                    if cell in hashmap[("col", col)]:
                        return False
                    hashmap[("col", col)].add(cell)
                    if cell in hashmap[("box", row//3, col//3)]:
                        return False
                    hashmap[("box", row//3, col//3)].add(cell)
        return True

