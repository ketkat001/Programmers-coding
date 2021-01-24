from itertools import permutations


def is_mapping(user_id, banned_id):
    for i in range(len(user_id)):
        if len(user_id[i]) != len(banned_id[i]):
            return False
        for j in range(len(user_id[i])):
            if banned_id[i][j] == '*':
                continue
            elif user_id[i][j] != banned_id[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for per_id in permutations(user_id, len(banned_id)):
        if is_mapping(per_id, banned_id):
            per_id = set(per_id)
            if per_id not in answer:
                answer.append(per_id)

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))