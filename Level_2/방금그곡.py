def cal_time(start_time, end_time):
    hour = int(end_time.split(':')[0]) - int(start_time.split(':')[0])
    mt = int(end_time.split(':')[1]) - int(start_time.split(':')[1])
    result = hour * 60 + mt
    return [result]


def change_melody(music):
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    music = music.replace('A#', 'a')
    return music


def solution(m, musicinfos):
    answer = '(None)'
    music_list = [[] for _ in range(len(musicinfos))]

    for i in range(len(music_list)):
        music_list[i] = musicinfos[i].split(',')
        music_list[i][:2] = cal_time(music_list[i][0], music_list[i][1])
    for i in range(len(music_list)):
        music_list[i][2] = change_melody(music_list[i][2])

    for i in range(len(music_list)):
        music_length = music_list[i][0]
        if music_length > len(music_list[i][2]):
            music_list[i][2] = music_list[i][2] * (music_length // len(music_list[i][2]) + 1)
        music_list[i][2] = music_list[i][2][:music_length]

    target_music = change_melody(m)
    result = []
    for music in music_list:
        if target_music in music[2]:
            result.append([music[0], music[1]])
    if result:
        answer = sorted(result, key=lambda x:-x[0])[0][1]
    return answer

print(solution('ABCDEFG#', ['12:00,12:14,HELLO,CDEFGAB#','13:00,13:05,WORLD,ABCDE#F']))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B#", ["03:00,00:00,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))