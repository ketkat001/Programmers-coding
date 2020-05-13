def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solution(arr):
    num1 = arr.pop()
    while arr:
        num2 = arr.pop()
        num1 = lcm(num1, num2)
    return num1


print(solution([2, 6, 8, 14]))
