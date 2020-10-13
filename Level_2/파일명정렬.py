def solution(files):
    answer = []
    compare_list = [[] for _ in range(len(files))]
    for i in range(len(files)):
        idx = 0
        num_idx, num_length = 101, 0
        while idx <= len(files[i]):
            if idx == len(files[i]):
                compare_list[i].append(files[i][num_idx-num_length+1:])
                break
            if files[i][idx].isnumeric():
                num_idx = idx
                num_length += 1
            elif (files[i][idx].isnumeric() == False or num_length == 5) and num_idx < idx:
                compare_list[i].append(files[i][num_idx-num_length+1:idx])
                break
            if num_length == 1:
                compare_list[i].append(files[i][:idx])
            idx += 1
        if idx < len(files[i]):
            compare_list[i].append(files[i][idx:])
    compare_list = sorted(compare_list, key=lambda x: (x[0].lower(), int(x[1])))
    for file in compare_list:
        answer.append(''.join(file))
    return answer


print(solution(['img12.png', 'img10.png', 'img02.png', 'img1', 'IMG01.GIF', 'img2.JPG', 'abc123defg123.jpg']))
