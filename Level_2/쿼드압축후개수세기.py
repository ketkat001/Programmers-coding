def solution(arr):
    global one, zero
    arr_length = len(arr)
    if arr_length == 1:
        if arr[0][0] == 1:
            one += 1
        else:
            zero += 1
    else:
        temp = arr[0][0]
        stop_flag = 0
        for i in range(arr_length):
            for j in range(arr_length):
                if arr[i][j] != temp:
                    solution([row[:arr_length // 2] for row in arr[:arr_length // 2]])
                    solution([row[arr_length // 2:] for row in arr[:arr_length // 2]])
                    solution([row[:arr_length // 2] for row in arr[arr_length // 2:]])
                    solution([row[arr_length // 2:] for row in arr[arr_length // 2:]])
                    stop_flag = 1
                    break
            if stop_flag == 1:
                break
        else:
            if temp == 0:
                zero += 1
            else:
                one += 1
    return [zero, one]

one, zero = 0, 0

print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
