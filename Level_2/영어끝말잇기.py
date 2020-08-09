def solution(n, words):
    use_words = []
    times = 1
    while True:
        for i in range(1, n+1):
            next_word = words.pop(0)
            if next_word in use_words:
                return [i, times]
            if use_words and use_words[-1][-1] != next_word[0]:
                return [i, times]
            use_words.append(next_word)
            if not words:
                return [0, 0]
        times += 1


print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
