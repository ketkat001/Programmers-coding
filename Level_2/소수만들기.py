from itertools import combinations


def decimal():
    decimal_list = [1] * 50001
    for i in range(2, 50001):
        if decimal_list[i] == 1:
            target_number = i * 2
            cnt = 2
            while target_number < 50001:
                decimal_list[target_number] = 0
                cnt += 1
                target_number = i * cnt
    return decimal_list


def solution(nums):
    answer = 0
    decimal_list = decimal()
    for comb in combinations(nums, 3):
        num = sum(comb)
        if decimal_list[num] == 1:
            answer += 1
    return answer


print(solution([1, 2, 3, 4]))