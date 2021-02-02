def solution(s):
    answer = ''
    cnt = 0
    for i in s:
        if cnt == 0 or cnt % 2 == 0:
            answer += i.upper() 
        else:
            answer += i.lower()
        if i == ' ':
            cnt = 0
        else:
            cnt += 1

    return answer

print(solution('try hello world') == 'TrY HeLlO WoRlD') # 'TrY HeLlO WoRlD'