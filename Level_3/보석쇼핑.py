def solution(gems):
    gem_cnt = len(set(gems))
    start, end = 0, 0
    answer = [0, len(gems) - 1]
    gem_dic = {gems[0]: 1}
    while start < len(gems) and end < len(gems):
        if len(gem_dic) == gem_cnt:
            if answer[1] - answer[0] > end - start:
                answer[0], answer[1] = start, end
            if gem_dic[gems[start]] == 1:
                del gem_dic[gems[start]]
            else:
                gem_dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in gem_dic.keys():
                gem_dic[gems[end]] += 1
            else:
                gem_dic[gems[end]] = 1

    return [answer[0] + 1, answer[1] + 1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))