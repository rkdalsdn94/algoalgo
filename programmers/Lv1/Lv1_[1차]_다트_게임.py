import re

def solution(dartResult):
    answer = []
    word = {
        'S': '**1',
        'D': '**2',
        'T': '**3',
        '#': '*-1'
    }
    s = re.sub('([SDT][*#]?)', r'\g<1> ', dartResult).split()
    for i in s:
        for j in i:
            i = i.replace(j, word.get(j, j))
            
        if i[-1] == '*':
            i += '2'
            if answer:
                answer[-1] = answer[-1][:-1] + '*2+'
        i += '+'
        answer.append(i)
    
    return eval(''.join(answer)[:-1])

print(solution('1S2D*3T')) # 37
print(solution('1D2S#10S')) # 9
print(solution('1D2S0T')) # 3
print(solution('1S*2T*3S')) # 23
print(solution('1D#2S*3S')) # 5
print(solution('1T2D3D#')) # -4
print(solution('1D2S3T*')) # 59