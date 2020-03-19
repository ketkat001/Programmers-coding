def solution(participant, completion):
    dict_list = dict()
    for person in completion:
        if person not in dict_list:
            dict_list[person] = 1
        else:
            dict_list[person] += 1
    for person in participant:
        if person not in dict_list or dict_list[person] == 0:
            return person
        else:
            dict_list[person] -= 1

print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))