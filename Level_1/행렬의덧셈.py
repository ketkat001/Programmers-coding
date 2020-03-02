def solution(arr1, arr2):
    length = len(arr1)
    length2 = len(arr1[0])
    answer = [[] for _ in range(length)]
    for i in range(length):
        for j in range(length2):
            answer[i].append(arr1[i][j]+arr2[i][j])
    return answer


print(solution([[1], [2]], [[3], [4]]))