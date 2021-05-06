from itertools import combinations


def make_cases(information):
    cases = []
    for k in range(5):
        for comb in combinations([0, 1, 2, 3], k):
            info = information[:]
            for c in comb:
                info[c] = '-'
            cases.append(''.join(info))
    return cases


def solution(info, query):
    answer = []
    search_dict = {}
    for information in info:
        information = information.split()
        cases = make_cases(information[:4])
        score = int(information[4])
        for case in cases:
            if case in search_dict:
                search_dict[case].append(score)
            else:
                search_dict[case] = [score]

    for key in search_dict.keys():
        search_dict[key].sort()

    for q in query:
        inf = q.split(' and ')
        inf[3:5] = inf[3].split(' ')
        query_score = int(inf[4])
        query_info = ''.join(inf[:4])
        if query_info in search_dict:
            score_list = search_dict[query_info]
            start, end = 0, len(score_list)
            while start < end:
                mid = (start + end) // 2
                if score_list[mid] >= query_score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(score_list) - start)
        else:
            answer.append(0)

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210",
                "python frontend senior chicken 150", "cpp backend senior pizza 260",
                "java backend junior chicken 80", "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
                "- and - and - and chicken 100", "- and - and - and - 150"]))
