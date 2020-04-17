def solution(skill, skill_trees):
    answer = 0
    for trees in skill_trees:
        idx = 0
        temp = 0
        for word in trees:
            if word in skill:
                if skill[idx] == word:
                    idx += 1
                    continue
                else:
                    temp = 1
                    break
        if temp == 0:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))