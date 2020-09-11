import copy


def airport(start, tickets, result, answer):
    if not tickets:
        result.append(start[1])
        answer.append(result)
        return
    else:
        starting = []
        for i in range(len(tickets)):
            if tickets[i][0] == start[1]:
                starting.append(tickets[i])
        for start in starting:
            ticket = copy.deepcopy(tickets)
            ticket.remove(start)
            copy_result = copy.deepcopy(result)
            copy_result.append(start[0])
            airport(start, ticket, copy_result, answer)


def solution(tickets):
    answer = []
    starting = []
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            starting.append(tickets[i])
    for start in starting:
        ticket = copy.deepcopy(tickets)
        ticket.remove(start)
        result = ['ICN']
        airport(start, ticket, result, answer)
    answer.sort()
    return answer[0]


print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))