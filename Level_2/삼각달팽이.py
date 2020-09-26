dx = [1, 0, -1]
dy = [0, 1, -1]

def solution(n):
    answer = []
    snail_list = [[0] * i for i in range(1, n+1)]
    x, y = 0, 0
    num = 1
    direction = 0
    end_point = (1+n) * (n//2) + ((1+n) // 2) * (n % 2)
    while num < end_point:
        snail_list[x][y] = num
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if 0 <= next_x < n and 0 <= next_y < n:
            if snail_list[next_x][next_y] == 0:
                x, y = next_x, next_y
                num += 1
            else:
                direction = (direction + 1) % 3
        else:
            direction = (direction + 1) % 3
    snail_list[x][y] = end_point
    for snail in snail_list:
        answer += snail
    return answer


print(solution(6))