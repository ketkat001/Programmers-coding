def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True


print(solution(["123", "456", "789"]))