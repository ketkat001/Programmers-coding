import heapq


def solution(jobs):
    jobs.sort()
    time, now, spot, job_length = 0, 0, 0, len(jobs)
    ready_queue = []
    while spot < job_length:
        for i in range(spot, job_length):
            if now >= jobs[i][0]:
                heapq.heappush(ready_queue, jobs[i][1])
                time += now - jobs[i][0]
                spot += 1
            else:
                break
        if ready_queue:
            queue_length = len(ready_queue)
            next_job = heapq.heappop(ready_queue)
            time += queue_length * next_job
            now += next_job
        else:
            now += 1
    while ready_queue:
        queue_length = len(ready_queue)
        next_job = heapq.heappop(ready_queue)
        time += queue_length * next_job
    return time // job_length


print(solution([[0, 3], [1, 9], [2, 6]]))
