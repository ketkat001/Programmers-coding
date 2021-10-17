import heapq


def solution(operations):
    queue = []
    max_queue = []
    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(queue, int(operation[2:]))
            heapq.heappush(max_queue, -int(operation[2:]))
        else:
            if len(queue) == 0:
                continue
            elif operation[2:] == '1':
                max_value = heapq.heappop(max_queue)
                queue.remove(-max_value)
            elif operation[2:] == '-1':
                min_value = heapq.heappop(queue)
                max_queue.remove(-min_value)

    if len(queue) == 0:
        return [0, 0]
    else:
        return [max(queue), min(queue)]

    return answer


print(solution(["I 7","I 5","I -5","D -1"]))