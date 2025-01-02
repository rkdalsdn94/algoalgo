# 백준 - 실버5 - Counting Monuments - 20376 - 자료 구조(집합), 문자열 문제
'''
자료 구조(집합), 문자열 문제

단순한 집합 문제이다. 입력을 받을 때마다 집합에 추가하고 집합의 길이를 출력하면 된다.
PyPy3로 제출해야 된다.

핵심 아이디어
    - 중복을 제거하기 위해 집합을 사용한다.
    - 입력을 받을 때마다 집합에 추가한다.
    - 집합의 길이를 출력한다.

풀이 과정
    1. 입력을 받는다.
    2. 집합을 생성한다.
    3. 입력을 받을 때마다 집합에 추가한다.
    4. 집합의 길이를 출력한다.

in
    2016-12-30 Tour Eiffel
    2016-12-31 Tour Saint-Jacques
    2016-12-31 Centre Georges Pompidou
    2018-01-15 Tour Eiffel
    2018-01-15 Invalides
    2018-01-15 Arc de Triomphe
    2018-01-16 Tour Saint-Jacques
    2018-01-16 Panthéon
    2018-01-17 Sacré Cœur
out
    7
'''

res = set()

while 1:
    try:
        date, *city = input().split()
        res.add(' '.join(city))
    except:
        break

print(len(res))
