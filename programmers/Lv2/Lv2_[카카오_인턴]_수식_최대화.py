import re
from itertools import permutations
def solution(expression):
    answer = []
    s = re.split('([-+*])', expression)
    ck_list = list(permutations('-+*', 3))
    
    for i in ck_list:
        temp = s[:]
        for j in i:
            while j in temp:
                idx = temp.index(j)
                temp[idx-1] = str(eval(temp[idx-1] + j + temp[idx+1]))
                del temp[idx:idx+2]
        answer.append(abs(int(temp[0])))
    return max(answer)

print(solution("100-200*300-500+20")) # 60420
print(solution("50*6-3*2")) # 300