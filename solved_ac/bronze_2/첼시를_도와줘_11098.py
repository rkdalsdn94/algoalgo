# 백준 - 브론즈2 - 첼시를 도와줘! - 11098 - 문자열, 단순 구현 문제
'''
문자열, 단순 구현 문제

단순한 구현, 문자열 문제이다.
    - 선수의 가격과 이름을 입력받는다.
    - 가장 비싼 선수의 이름을 출력하는 문제이다.
    - 문자열을 정렬할 때 숫자가 아니라 문자 형태로 정렬하면 정렬이 제대로 안 된다.
        - 문자열의 정렬은 각 문자의 ASCII 코드 값에 따라 이루어진다.
        - 예제의 두 번째 테스트 케스트를 보면 정렬이 안 된다.
        - 즉, test = ['10', '9']를 정렬하면 ['10', '9']가 나온다. (원하는 결과가 아님)
    - 이 부분만 신경쓰고 풀면 된다.

풀이 과정
    1. t를 입력받는다.
    2. t만큼 반복문을 돌린다.
    3. n을 입력받는다.
    4. player에 n개의 리스트를 입력받는다.
    5. player를 정렬한다.
    6. player[-1][1]를 출력한다.

in
    2
    3
    10 Iversen
    1000000 Nannskog
    2000000 Ronaldinho
    2
    1000000 Maradona
    999999 Batistuta
out
    Ronaldinho
    Maradona
'''

t = int(input())
for _ in range(t):
    n = int(input())
    player = sorted([list(input().split()) for _ in range(n)], key=lambda x: int(x[0]))
    print(player[-1][1])
