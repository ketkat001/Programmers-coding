def find_square(board, x, y, height, width):
    num = []
    temp = 10
    for i in range(x, x+height):
        for j in range(y, y+width):
            if board[i][j] != 0:
                temp = board[i][j]
                num.append(board[i][j])
    if len(num) == 4:
        if sum(num) // len(num) == temp:
            return 1
    return 0


def solution(board):
    length = len(board)
    N = 0
    for a in range(length):
        N = max(N, max(board[a]))
    cnt = 0
    while True:
        temp = 0
        for i in range(length):
            for j in range(length):
                if i <= length-3:
                    if j <= length-2:
                        temp = find_square(board, i, j, 3, 2)
                        if temp == 1:
                            for p in range(i, i+3):
                                for q in range(j, j+2):
                                    board[p][q] = 0
                elif i <= length-2:
                    if j <= length-3:
                        temp = find_square(board, i, j, 2, 3)
                        if temp == 1:
                            cnt += 1
                            for p in range(i, i+2):
                                for q in range(j, j+3):
                                    board[p][q] = 0

        else:
            break


    return N - cnt


print(solution([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,4,0,0,0],
                [0,0,0,0,0,4,4,0,0,0],
                [0,0,0,0,3,0,4,0,0,0],
                [0,0,0,2,3,0,0,0,5,5],
                [1,2,2,2,3,3,0,0,0,5],
                [1,1,1,0,0,0,0,0,0,5]]
               ))