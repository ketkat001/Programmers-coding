def solution(nums):
    answer = 0
    max_num = len(nums)//2
    target_nums = len(set(nums))
    if max_num > target_nums:
        max_num = target_nums
    answer = max_num
    return answer


print(solution([3, 1, 2, 3]))
