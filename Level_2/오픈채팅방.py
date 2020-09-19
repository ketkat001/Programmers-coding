def solution(record):
    answer = []
    id_dict = dict()
    temp = []
    for messages in record:
        message = list(messages.split(' '))
        if message[0] == 'Enter':
            id_dict[message[1]] = message[2]  # this id have nickname
            temp.append(message[1]+' '+'님이 들어왔습니다.')
        elif message[0] == 'Leave':
            temp.append(message[1]+' '+'님이 나갔습니다.')
        else:
            id_dict[message[1]] = message[2]

    for temp_message in temp:
        mes = list(temp_message.split(' '))
        mes[0] = id_dict[mes[0]]
        answer.append(mes[0] + ' '.join(mes[1:]))

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))