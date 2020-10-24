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


print(solution(["2016-09-15 23:59:59.999 0.001s"]))
