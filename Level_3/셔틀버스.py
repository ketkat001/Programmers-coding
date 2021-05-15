import heapq


def solution(n, t, m, timetable):
    queue = []
    heapq.heapify(queue)
    bus_time = 540
    for time in timetable:
        time = int(time[:2]) * 60 + int(time[3:])
        heapq.heappush(queue, time)
    while n > 1:
        allow_passenger = m
        while queue:
            passenger = heapq.heappop(queue)
            if passenger > bus_time or allow_passenger == 0:
                heapq.heappush(queue, passenger)
                break
            else:
                allow_passenger -= 1
        n -= 1
        bus_time += t

    while m > 1 and queue:
        heapq.heappop(queue)
        m -= 1
    print(bus_time, queue)
    if queue:
        last_man = heapq.heappop(queue)
        if last_man > bus_time:
            last_time = bus_time
        else:
            last_time = last_man - 1
    else:
        last_time = bus_time

    answer = str(last_time // 60).zfill(2) + ':' + str(last_time % 60).zfill(2)

    return answer

print(solution(1, 1, 1, ["23:59"]))
