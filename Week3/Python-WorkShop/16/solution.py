def main(board):
    def check_rows(board):
        for row in board:
            if len(set(row)) != 9 or sum(row) != 45:
                return False
        return True

    def check_columns(board):
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if len(set(column)) != 9 or sum(column) != 45:
                return False
        return True

    def check_regions(board):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                region = [board[row+i][col+j] for i in range(3) for j in range(3)]
                if len(set(region)) != 9 or sum(region) != 45:
                    return False
        return True

    if check_rows(board) and check_columns(board) and check_regions(board):
        return 'Finished!'
    else:
        return 'Try again!'