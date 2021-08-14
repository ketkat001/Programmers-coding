from itertools import combinations


def check_minimality(comb_list, candidate_keys):
    for i in range(1, len(comb_list)+1):
        for comb in combinations(comb_list, i):
            if list(comb) in candidate_keys:
                return True
    return False


def check_uniqueness(comb_list, columns):
    validate_list = [tuple(columns[comb][i] for comb in comb_list) for i in range(len(columns[0]))]
    if len(set(validate_list)) == len(columns[0]):
        return True
    return False


def solution(relation):
    column, row = len(relation), len(relation[0])
    candidate_keys = []
    columns = {i: [] for i in range(row)}
    for i in range(row):
        temp = []
        for j in range(column):
            temp.append(relation[j][i])
        columns[i] = temp
    for p in range(1, column+1):
        for comb in combinations(columns, p):
            if check_minimality(comb, candidate_keys):
                continue
            if not check_uniqueness(comb, columns):
                continue
            candidate_keys.append(list(comb))
    answer = len(candidate_keys)
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([['1', '1', '3'], ['3', '1', '2'], ['3', '2', '3']]))
print(solution([['a','aa'],['aa','a'],['a','a']]))
print(solution([["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]))
