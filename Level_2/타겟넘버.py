def solution(numbers, target):
    answer = target_dfs(numbers, target, 0)
    return answer


def target_dfs(numbers, target, number):
    global result
    if not numbers:
        if target == number:
            result += 1
            return
    else:
        num = numbers[-1]
        numbers = numbers[:-1]
        target_dfs(numbers, target, number+num)
        target_dfs(numbers, target, number-num)

    return result

result = 0
print(solution([1, 1, 1, 1, 1], 3))
