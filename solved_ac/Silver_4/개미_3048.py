'''
구현, 문자열, 시뮬레이션 문제

두 문자열은 서로 다른 값을 가지고 있기 때문에
res에 n1, n2 두 문자열을 합친 상태에서
t만큼 반복하는데 swap할 idx를 찾은 다음 swap 후 출력하면 된다.

idx 찾는 조건은 1부터 res만큼 반복하면서
반복되는 현재 idx가 n2글자 안에 있고, 현재 - 1 idx가 n1글자 안에 있으면 만족한돠.
'''

# a, b = map(int, input().split())
# n1, n2 = list(input())[::-1], list(input())
# t = int(input())

# 테스트
# a, b = 3, 3
# n1, n2 = list('ABC')[::-1], list('DEF')
# t = 0 # CBADEF
# a, b = 3, 3
# n1, n2 = list('ABC')[::-1], list('DEF')
# t = 2 # CDBEAF
a, b = 3, 4
n1, n2 = list('JLA')[::-1], list('CRU0')
t = 3 # CARLUJ0

res = n1 + n2

for _ in range(t):
    idx = []

    for i in range(1, len(res)):
        if res[i] in n2 and res[i-1] in n1:
            idx.append(i)
    
    for i in idx:
        res[i-1], res[i] = res[i], res[i-1]

print(''.join(res))
