class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        box_map = defaultdict(set)

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    continue

                box_id = (i // 3) * 3 + (j // 3)

                if v in row_map[i] or v in col_map[j] or v in box_map[box_id]:
                    return False

                row_map[i].add(v)
                col_map[j].add(v)
                box_map[box_id].add(v)

        return True