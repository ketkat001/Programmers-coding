from itertools import permutations


def calculator(operators, n, expression):
    if n == 2:
        result = eval(expression)
        return str(result)
    else:
        if operators[n] == '*':
            result = eval('*'.join([calculator(operators, n+1, e) for e in expression.split('*')]))
        elif operators[n] == '+':
            result = eval('+'.join([calculator(operators, n+1, e) for e in expression.split('+')]))
        else:
            result = eval('-'.join([calculator(operators, n+1, e) for e in expression.split('-')]))

    return str(result)


def solution(expression):
    answer = 0
    operators = ['*', '-', '+']
    for comb in permutations(operators, 3):
        priority_operator = list(comb)
        answer = max(answer, abs(int(calculator(priority_operator, 0, expression))))

    return answer




print(solution("100-200*300-500+20"))