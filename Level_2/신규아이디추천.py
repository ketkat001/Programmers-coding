import re


def delete_dot(new_id):
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    return new_id


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9._-]', "", new_id)

    flag = 0
    word = ''
    for string in new_id:
        if string == '.' and flag == 0:
            word += string
            flag = 1
        elif string == '.' and flag == 1:
            continue
        else:
            word += string
            flag = 0

    new_id = word
    if new_id:
        new_id = delete_dot(new_id)

    if not new_id:
        new_id += 'a'

    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = delete_dot(new_id)

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id


print(solution("...2332..2323....3232...."))