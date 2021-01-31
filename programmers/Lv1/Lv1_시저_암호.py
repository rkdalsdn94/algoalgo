def solution(s, n):
    answer = ''
    for i in s:
        for j in i:
            if j.islower():
                answer += chr((ord(j) - ord('a') + n)%26 + ord('a'))
            elif j.isupper():
                answer += chr((ord(j) - ord('A') + n)%26 + ord('A'))
            else:
                answer += j
    return answer
print(solution('AB', 1)) # 'BC'
print(solution('z', 1)) # 'a'
print(solution('a B z', 4)) # 'e F d'