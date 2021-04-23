def possible(s, mid):
    for i in range(0, len(s)-mid+1):
        word = s[i:i+mid]
        half = len(word) // 2
        if word[:half] == word[half:]:
            return True
    return False


def solution(s):
    answer = 0
    left, right = 1, len(s)+1
    while left < right - 1:
        mid = (left+right) // 2
        if possible(s, mid):
            left = mid
        else:
            right = mid
    return answer


print(solution("abccba"))