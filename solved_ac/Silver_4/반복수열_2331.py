'''
구현, 수학 문제

while 문으로 반복되는 값이 나오기 전까지 반복하고, 나올때 break를 건다.
그 후에 해당 res를 반복되기 전의 값들로 다시 초기화 한 후,
res의 길이를 출력하면 된다.

deque를 안써도 충분히 풀 수도 있는데, 이것 저것 사용해 보고 싶은 마음에 사용했다.
'''

from collections import deque

a, p = map(int, input().split())

# 테스트
# a, p = 57, 2

q = deque([a])
res = [a]

while 1:
    x = str(q.popleft())
    temp = 0

    for i in x:
        temp += int(i) ** p
    
    if temp in res:
        res = res[:res.index(temp)]
        break

    res.append(temp)
    q.append(temp)

print(len(res))
