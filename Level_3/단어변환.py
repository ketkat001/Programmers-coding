from collections import deque


def check_word(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
        if cnt > 1:
            return False
    if cnt == 1:
        return True
    return False


def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    if target not in words:
        return 0
    while queue:
        x, cnt = queue.popleft()
        for word in words:
            if check_word(x, word):
                if word == target:
                    return cnt+1
                queue.append([word, cnt+1])
    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "hhh", ["hhh", "hht"]))