def solution(clothes):
    answer = 1
    cloth_list = dict()
    for cloth in clothes:
        if cloth[1] not in cloth_list:
            cloth_list[cloth[1]] = [cloth[0]]
        else:
            cloth_list[cloth[1]].append(cloth[0])
    for key, value in cloth_list.items():
        answer *= len(value)+1
    return answer-1


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))