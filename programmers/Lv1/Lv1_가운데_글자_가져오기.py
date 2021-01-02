def solution(s):
    middle = len(s) // 2
    if len(s) % 2 == 0:
        return s[middle - 1] + s[middle]
    else:
        return s[middle]
