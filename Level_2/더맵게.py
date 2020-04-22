import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        num1 = heapq.heappop(scoville)
        if num1 >= K:
            break
        num2 = heapq.heappop(scoville)
        heapq.heappush(scoville, num1+(num2*2))
        answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1


print(solution([1, 2, 3, 9, 10, 12], 7))