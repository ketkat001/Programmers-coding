def solution(n, k, cmd):
    answer = ''
    table_dict = {0: [None, 1], n - 1: [n - 2, None]}
    for i in range(1, n - 1):
        table_dict[i] = [i - 1, i + 1]
    current = k
    stack = []
    for command in cmd:
        command = command.split(' ')
        if command[0] == 'D':
            for _ in range(int(command[1])):
                current = table_dict[current][1]
        elif command[0] == 'U':
            for _ in range(int(command[1])):
                current = table_dict[current][0]
        elif command[0] == 'C':
            stack.append([current, table_dict[current][0], table_dict[current][1]])
            if table_dict[current][0] is not None:
                table_dict[table_dict[current][0]][1] = table_dict[current][1]

            if table_dict[current][1] is not None:
                table_dict[table_dict[current][1]][0] = table_dict[current][0]
                next_current = table_dict[current][1]
            else:
                next_current = table_dict[current][0]

            del table_dict[current]
            current = next_current
        else:
            recovery = stack.pop()
            table_dict[recovery[0]] = [recovery[1], recovery[2]]
            if recovery[2] is not None:
                table_dict[recovery[2]][0] = recovery[0]
            if recovery[1] is not None:
                table_dict[recovery[1]][1] = recovery[0]
    for i in range(n):
        if i in table_dict:
            answer += 'O'
        else:
            answer += 'X'

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
