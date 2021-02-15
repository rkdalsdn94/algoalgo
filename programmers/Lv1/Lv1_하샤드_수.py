def solution(x):
    temp = sum([ int(i) for i in str(x) ])
    if x % temp == 0:
        return True
    return False
print(solution(10)) # True
print(solution(12)) # True
print(solution(11)) # False
print(solution(13)) # False