def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1])
    min_camera = -30001
    for i in range(len(routes)):
        if routes[i][0] <= min_camera <= routes[i][1]:
            continue
        else:
            answer += 1
            min_camera = routes[i][1]
    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))