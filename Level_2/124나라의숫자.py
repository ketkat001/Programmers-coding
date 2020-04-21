def solution(n):
    T = '124'
    q, r = divmod(n-1, 3)
    if q == 0:
        return T[r]
    else:
        return solution(q) + T[r]


print(solution(10))