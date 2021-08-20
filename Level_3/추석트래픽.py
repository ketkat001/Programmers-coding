import datetime


def transform_datetime(line):
    temp_list = line.split(' ')
    duration = float(temp_list[2][:-1])
    end = datetime.datetime.strptime(' '.join(temp_list[:2]),'%Y-%m-%d %H:%M:%S.%f')
    start = end - datetime.timedelta(seconds=duration-0.001)
    return [start, end]


def compare_time(time1, time2):
    if time1[1] < time2[0] - datetime.timedelta(seconds=0.999):
        return False
    return True


def solution(lines):
    answer = 1
    datetime_list = []
    for line in lines:
        datetime_list.append(transform_datetime(line))
    for i in range(len(datetime_list)-1):
        cnt = 1
        for j in range(i+1, len(datetime_list)):
            if compare_time(datetime_list[i], datetime_list[j]):
                cnt += 1
        answer = max(answer, cnt)
    return answer



print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
