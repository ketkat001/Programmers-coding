def checking(people, place):
    for p in range(len(people) - 1):
        for q in range(p + 1, len(people)):
            if abs(people[p][0] - people[q][0]) + abs(people[p][1] - people[q][1]) <= 2:
                p1, p2 = people[p], people[q]
                if p1[0] == p2[0] and place[p1[0]][(p1[1]+p2[1])//2] != 'X':
                    return True
                elif p1[1] == p2[1] and place[(p1[0]+p2[0])//2][p1[1]] != 'X':
                    return True
                elif p1[0] != p2[0] and p1[1] != p2[1]:
                    if place[p1[0]][p2[1]] != 'X' or place[p2[0]][p1[1]] != 'X':
                        return True
    return False


def solution(places):
    answer = []
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append([i, j])
        if checking(people, place):
            answer.append(0)
        else:
            answer.append(1)
    return answer


print(solution(	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
