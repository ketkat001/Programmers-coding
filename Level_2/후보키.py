from itertools import combinations


def solution(relation):
    answer = []
    temp = [[] for _ in range(len(relation[0]))]
    for i in range(len(relation)):
        for j in range(len(relation[0])):
            temp[j].append(relation[i][j])
    for i in range(1, len(relation)):
        for comb in combinations(temp, i):
            comb = list(comb)
            temp_list = []
            for l in range(len(comb[0])):
                temp_word = ''
                for com in comb:
                    temp_word += com[l]
                temp_list.append(temp_word)
            if len(set(temp_list)) == len(relation):
                answer.append(comb)
    remove_list = []
    for i in range(len(answer)-1):
        for j in range(i+1, len(answer)):
            count = 0
            for p in range(len(answer[i])):
                for q in range(len(answer[j])):
                    if answer[i][p] == answer[j][q]:
                        count += 1
            if count == len(answer[i]):
                remove_list.append(answer[j])
    for rl in remove_list:
        if rl in answer:
            answer.remove(rl)
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([['1', '1', '3'], ['3', '1', '2'], ['3', '2', '4']]))
