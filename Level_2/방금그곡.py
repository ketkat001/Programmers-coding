from datetime import datetime


def solution(m, musicinfos):
    answer = []
    music_list = [[] for _ in range(len(musicinfos))]
    temp = []
    for i in range(len(m)):
        if m[i] != '#':
            temp.append(m[i])
        else:
            temp[-1] += '#'
    m = temp
    for i in range(len(music_list)):



        music_list[i] = musicinfos[i].split(',')
        music_list[i][3] = list(music_list[i][3])
        temp = []
        for j in range(len(music_list[i][3])):
            if music_list[i][3][j] != '#':
                temp.append(music_list[i][3][j])
            else:
                temp[-1] += '#'
        music_list[i][3] = temp

    for i in range(len(music_list)):
        start_time, end_time = music_list[i][0], music_list[i][1]
        music_list[i][0] = str(datetime.strptime(end_time, '%H:%M') - datetime.strptime(start_time, '%H:%M'))[2:4]
        music_list[i][0] = int(music_list[i][0])
        music_length = len(music_list[i][3])
        if music_list[i][0] > music_length:
            music_list[i][3] = music_list[i][3] * (music_list[i][0] // music_length + 1)
        music_list[i][3] = music_list[i][3][:music_list[i][0]]
    for music in music_list:
        target_length = len(m)
        for i in range(len(music[3]) - target_length):
            if m == music[3][i:i + target_length]:
                if m[-1] != '#' and music[3][i + target_length] != '#':
                    answer.append([music[0], music[2]])
    if answer:
        answer = sorted(answer, key=lambda x: x[0], reverse=True)[0][1]
    else:
        answer = '(None)'

    return answer

print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB','13:00,13:05,WORLD,ABCDEF']))
print(solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB','13:00,13:05,WORLD,ABCDEF']))