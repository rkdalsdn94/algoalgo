def solution(phone_book):
    phone_book.sort()
    temp, phone_book = phone_book[0], phone_book[1:]
    # print(temp, phone_book)

    for i in phone_book:
        if i[0:len(temp)] == temp:
            return False
    return True


print(solution(['119', '97674223', '1195524421']))
print(solution(['123', '456', '789']))
print(solution(['12', '123', '1235', '567', '88']))
