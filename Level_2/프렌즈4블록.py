def find_4blocks(m, n, board, answer):
    validate_of_board = False
    check_4blocks = [[0]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if board[i-1][j] == board[i-1][j-1] == board[i][j] == board[i][j-1] != 0:
                check_4blocks[i-1][j] = check_4blocks[i][j] = check_4blocks[i-1][j-1] = check_4blocks[i][j-1] = 1
    for i in range(m):
        for j in range(n):
            if check_4blocks[i][j] == 1:
                validate_of_board = True
                board[i][j] = 0
                answer += 1
    board = push_board(m, n, board)
    return validate_of_board, board, answer


def push_board(m, n, board):
    for i in range(m-1, 0, -1):
        for j in range(n):
            if board[i][j] == 0:
                next_x = i-1
                while next_x >= 0:
                    if board[next_x][j] != 0:
                        board[i][j], board[next_x][j] = board[next_x][j], 0
                        break
                    next_x -= 1
    return board


def solution(m, n, board):
    validate_of_board = True
    board = [list(word) for word in board]
    answer = 0
    while validate_of_board:
        validate_of_board, board, answer = find_4blocks(m, n, board, answer)
    return answer


print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))