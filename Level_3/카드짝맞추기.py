from collections import deque
from itertools import permutations
import copy


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def cal_operation(board, card_order, r, c, min_operation):
    queue = deque([[r, c, 0]])
    target = card_order.pop()
    open_flag, cnt = 0, 0
    visited = [[0]*4 for _ in range(4)]
    visited[r][c] = 1
    while queue:
        if target == 0:
            break
        x, y, cnt = queue.popleft()
        if board[x][y] == target and open_flag == 0:
            queue = deque([[x, y, cnt+1]])
            visited = [[0] * 4 for _ in range(4)]
            open_flag = 1
            board[x][y] = 0
            continue
        elif board[x][y] == target and open_flag == 1:
            queue = deque([[x, y, cnt+1]])
            open_flag = 0
            visited = [[0] * 4 for _ in range(4)]
            board[x][y] = 0
            if card_order:
                target = card_order.pop()
            else:
                target = 0
            continue
        else:
            for d in range(4):
                next_x, next_y = x + dx[d], y + dy[d]
                if 0 <= next_x < 4 and 0 <= next_y < 4 and not visited[next_x][next_y]:
                    queue.append([next_x, next_y, cnt+1])
                    visited[next_x][next_y] = 1
                while True:
                    if next_x < 0 or next_x >= 4 or next_y < 0 or next_y >= 4:
                        queue.append([next_x-dx[d], next_y-dy[d], cnt+1])
                        break
                    if board[next_x][next_y] != 0:
                        queue.append([next_x, next_y, cnt+1])
                        break
                    next_x, next_y = next_x + dx[d], next_y + dy[d]

    if min_operation > cnt:
        return cnt

    return min_operation


def solution(board, r, c):
    answer = 99999
    card_num = set([])
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_num.add(board[i][j])
    card_num = list(card_num)
    for perm in permutations(card_num, len(card_num)):
        perm = list(perm)
        b_d = copy.deepcopy(board)
        answer = cal_operation(b_d, perm, r, c, answer)

    return answer+1


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
