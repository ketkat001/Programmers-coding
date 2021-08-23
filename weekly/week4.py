def solution(table, languages, preference):
    answer = []
    favor_dict = {}
    score_dict = {}
    for favor in table:
        favor = favor.split(' ')
        favor_dict[favor[0]] = {}
        score_dict[favor[0]] = 0
        for i in range(1, 6):
            favor_dict[favor[0]][favor[i]] = 6 - i

    for p in range(len(languages)):
        for job in favor_dict:
            if languages[p] in favor_dict[job]:
                score_dict[job] += favor_dict[job][languages[p]] * preference[p]

    max_value = 0
    for key, value in score_dict.items():
        if value > max_value:
            max_value = value
            answer = [key]
        elif value == max_value:
            answer.append(key)
    answer.sort()
    return answer[0]


# print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
#                 "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
#                 "GAME C++ C# JAVASCRIPT C JAVA"],
#                ["PYTHON", "C++", "SQL"], [7, 5, 5]))

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
