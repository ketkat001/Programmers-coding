def solution(weights, head2head):
    answer = []
    cal_list = []
    for i in range(len(weights)):
        total_match, win_match = 0, 0
        temp = [0, 0, weights[i], i+1]
        for j in range(len(weights)):
            if head2head[i][j] == 'W':
                win_match += 1
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                total_match += 1
            if head2head[i][j] == 'W' and weights[j] > weights[i]:
                temp[1] += 1
        if total_match != 0:
            temp[0] = win_match / total_match

        cal_list.append(temp)
    cal_list.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    for p in range(len(cal_list)):
        answer.append(cal_list[p][3])
    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))