def solution(s):
    return s.upper().count('P') == s.upper().count('Y')


print(solution('pPoooyY'))
print(solution('Pyy'))
