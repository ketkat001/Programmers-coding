from itertools import permutations


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    number_list = []
    for i in range(1, len(numbers)+1):
        for comb in permutations(numbers, i):
            comb = int(''.join(list(comb)))
            if comb not in number_list:
                if comb != 0 and comb != 1:
                    number_list.append(comb)
    for numb in number_list:
        for j in range(2, numb):
            if numb % j == 0:
                break
        else:
            answer += 1

    return answer


print(solution('101'))