def solution(s):
    temp = 0
    for i in s:
        if i == '(':
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            return False
    if not temp:
        return True
    return False

print(solution('()()')) # true
print(solution('(())()')) # true
print(solution(')()(')) # false
print(solution('(()(')) # false