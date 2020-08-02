from collections import deque


def solution(cacheSize, cities):
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    cache_queue = deque()
    answer = 0
    for city in cities:
        if city not in cache_queue:
            cache_queue.append(city)
            answer += 5
        else:
            cache_queue.remove(city)
            cache_queue.append(city)
            answer += 1
        if len(cache_queue) > cacheSize:
            cache_queue.popleft()
    return answer


print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))