def time_to_second(data):
    h, m, s = map(int, data.split(':'))
    return 3600 * h + 60 * m + s


def second_to_time(data):
    h = str(data // 3600).zfill(2)
    data = data % 3600
    m = str(data // 60).zfill(2)
    s = str(data % 60).zfill(2)
    return ':'.join([h, m, s])


def solution(play_time, adv_time, logs):
    play_time = time_to_second(play_time)
    person_dp = [0] * (play_time + 1)
    for log in logs:
        start, end = log.split('-')
        start = time_to_second(start)
        end = time_to_second(end)
        person_dp[start] += 1
        person_dp[end] -= 1

    for i in range(1, play_time + 1):
        person_dp[i] += person_dp[i-1]

    for i in range(1, play_time + 1):
        person_dp[i] += person_dp[i-1]

    adv_time = time_to_second(adv_time)
    max_time = 0
    max_view = person_dp[adv_time]

    for start_time in range(1, play_time):
        end_time = start_time + adv_time if start_time + adv_time < play_time else play_time
        sum_view = person_dp[end_time] - person_dp[start_time]
        if max_view < sum_view:
            max_view = sum_view
            max_time = start_time + 1

    return second_to_time(max_time)


print(solution("00:00:00", "00:00:00", []))

