def solution(genres, plays):
    answer = []
    music_dict, music_count_dict = {}, {}
    music_rank = []
    for i in range(len(genres)):
        if genres[i] not in music_dict:
            music_dict[genres[i]] = [[plays[i], i]]
        else:
            music_dict[genres[i]].append([plays[i], i])
        if genres[i] not in music_count_dict:
            music_count_dict[genres[i]] = plays[i]
        else:
            music_count_dict[genres[i]] += plays[i]

    for genre, music in music_dict.items():
        music.sort(key=lambda x:[-x[0], x[1]])

    for genre, count in music_count_dict.items():
        music_rank.append([count, genre])
    music_rank.sort(reverse=True)

    for music in music_rank:
        if len(music_dict[music[1]]) < 2:
            answer.append(music_dict[music[1]][0][1])
        else:
            for i in range(2):
                answer.append(music_dict[music[1]][i][1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))