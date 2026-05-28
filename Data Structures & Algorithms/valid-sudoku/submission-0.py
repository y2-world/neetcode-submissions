class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 各行ごとに見た数字を記録するためのsetを9個用意する
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                # 9x9の全マスを左上から順にチェック
                value = board[r][c]
                if value == '.':
                    continue
                # どの3x3ブロックかをチェック
                box_index = (r // 3) * 3 + (c // 3)
                # どこかで既に同じ数字が出てないかチェック
                if (
                    # r行目/c列目/box_indexに同じ数字があるか
                    value in rows[r]
                    or value in cols[c]
                    or value in boxes[box_index]
                ):
                    return False
                # 現在の数字を行・列・3x3ブロックに記録する
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)
        return True
                


