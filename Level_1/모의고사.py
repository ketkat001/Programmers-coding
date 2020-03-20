def solution(answers):
    ans_len = len(answers)
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one = one * (ans_len // len(one)) + one[:ans_len % len(one)]
    two = two * (ans_len // len(two)) + two[:ans_len % len(two)]
    three = three * (ans_len // len(three)) + three[:ans_len % len(three)]

    cnt = [[1, 0], [2, 0], [3, 0]]
    for i in range(ans_len):
        if answers[i] == one[i]:
            cnt[0][1] += 1
        if answers[i] == two[i]:
            cnt[1][1] += 1
        if answers[i] == three[i]:
            cnt[2][1] += 1
    cnt.sort(key=lambda x: (-x[1], x[0]))
    answer = [cnt[0][0]]
    for i in range(1, 3):
        if cnt[0][1] == cnt[i][1]:
            answer.append(cnt[i][0])

    return answer


print(solution([1, 1, 2, 4, 4, 2, 2]))