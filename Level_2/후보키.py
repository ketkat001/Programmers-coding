from itertools import combinations


def solution(relation):
    candidate_key = []
    columns = [[relation[i][j] for i in range(len(relation))] for j in range(len(relation[0]))]
    print(columns)
    for i in range(1, len(columns)+1):
        for comb in combinations(columns, i):
            key = list(comb)
            validate_key = validate_candidate_key(key)
            if validate_key:
                minimality_key = check_minimality(key, candidate_key)
                if minimality_key:
                    candidate_key.append(key)
    print(candidate_key)
    answer = len(candidate_key)
    return answer


def validate_candidate_key(key):
    validate_list = []
    for i in range(len(key[0])):
        word = ''
        for j in range(len(key)):
            word += key[j][i]
        validate_list.append(word)
    if len(set(validate_list)) == len(key[0]):
        return True
    return False


def check_minimality(key, candidate_key):
    for i in range(1, len(key)+1):
        for comb in combinations(key, i):
            if list(comb) in candidate_key:
                return False
    return True

#print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([['1', '1', '3'], ['3', '1', '2'], ['3', '2', '3']]))
print(solution([['a','aa'],['aa','a'],['a','a']]))
