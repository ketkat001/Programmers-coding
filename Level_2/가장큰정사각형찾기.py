def solution(board):
    column, row = len(board), len(board[0])
    max_num = 0
    for i in range(column):
        if board[i][0] == 1:
            max_num = 1
    for j in range(row):
        if board[0][j] == 1:
            max_num = 1
    for i in range(1, column):
        for j in range(1, row):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1
                max_num = max(max_num, board[i][j])
    answer = max_num ** 2
    return answer


print(solution([[1, 0], [0, 0]]))