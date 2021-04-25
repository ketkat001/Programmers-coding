from collections import deque

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]


def bfs(min_price, n, board):
    queue = deque([])
    visited = [[float('inf')]*n for _ in range(n)]
    visited[0][0] = 0
    if board[0][1] == 0:
        queue.append([0, 1, 3, 100])
        visited[0][1] = 100
    if board[1][0] == 0:
        queue.append([1, 0, 1, 100])
        visited[1][0] = 100
    while queue:
        x, y, direction, price = queue.popleft()
        if price > min_price:
            continue
        if x == n-1 and y == n-1 and min_price > price:
            min_price = price
        else:
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if d == direction:
                    cost = price + 100
                else:
                    cost = price + 600
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny] >= cost:
                    visited[nx][ny] = cost
                    queue.append([nx, ny, d, cost])

    return min_price


def solution(board):
    n = len(board)
    answer = bfs(float('inf'), n, board)
    return answer


print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
