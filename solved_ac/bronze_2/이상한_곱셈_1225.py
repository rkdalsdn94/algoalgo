# 백준 - 이상한 곱셈 - 1225 - 브론즈2 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

단순 구현 문제이다.
a를 한 글자씩 반복하면서 각각 b를 곱한 값을 res에 담고 출력하면 된다.

int로 바꾼 다음 그 수들을 sum 하고 해당 값 끼리 곱하면 된다.
 - 위 방법이 속도가 더 빠르다

a, b = map(list, input().split())
a = sum([ int(i) for i in a ])
b = sum([ int(i) for i in b ])
print(a * b) --> 이 코드가 더 빠르다.
이 방식은 Python3로 해도 통과된다.

아래 코드는 Python3 일때는 시간 초과가 나오고, PyPy3로 해야 통과할 수 있다. 
'''

a, b = input().split()

# 테스트
# a, b = '123', '45' # 54

res = 0

for i in a:
    for j in b:
        res += int(i) * int(j)

print(res)
