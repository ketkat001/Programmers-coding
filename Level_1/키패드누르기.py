def solution(numbers, hand):
    key_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_hand, right_hand = [3, 0], [3, 2]
    answer = ''
    for number in numbers:
        if number in [0, 2, 5, 8]:  #만약 number가 2, 5, 8, 0 중에 하나라면
            for i in range(4):
                for j in range(3):
                    if key_pad[i][j] == number:
                        left_dis = abs(left_hand[0]-i) + abs(left_hand[1]-j)
                        right_dis = abs(right_hand[0]-i) + abs(right_hand[1]-j)
                        if left_dis > right_dis:
                            right_hand = [i, j]
                            answer += 'R'
                        elif left_dis < right_dis:
                            left_hand = [i, j]
                            answer += 'L'
                        else:
                            if hand == 'right':
                                right_hand = [i, j]
                                answer += 'R'
                            else:
                                left_hand = [i, j]
                                answer += 'L'
        elif number in [1, 4, 7]:
            for i in range(4):
                for j in range(3):
                    if number == key_pad[i][j]:
                        left_hand = [i, j]
                        answer += 'L'
        else:
            for i in range(4):
                for j in range(3):
                    if number == key_pad[i][j]:
                        right_hand = [i, j]
                        answer += 'R'
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'right'))