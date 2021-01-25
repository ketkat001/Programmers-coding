def solution(k, room_number):
    answer = []
    room = {}
    for number in room_number:
        if number not in room:
            room[number] = number + 1
            answer.append(number)
        else:
            visit = [number]
            while True:
                index = number
                number = room.get(number, 0)
                if not number:
                    answer.append(index)
                    room[index] = index + 1
                    for num in visit:
                        room[num] = index + 1
                    break
                else:
                    visit.append(number)
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))