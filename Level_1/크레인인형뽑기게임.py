def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        temp = 0
        for i in range(len(board)):
            if board[i][move-1] != 0:
                temp = board[i][move-1]
                board[i][move-1] = 0
                break
        if temp == 0:
            continue
        else:
            if not basket:
                basket.append(temp)
            elif basket[-1] == temp:
                basket.pop()
                answer += 2
            else:
                basket.append(temp)
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))