# 백준 - 실버4 - 철벽 보안 알고리즘 - 9322 - 문자열, 자료 구조(해시) 문제
'''
문자열, 자료 구조(해시) 문제

첫 번째 키와 두 번째 키를 힌트로 암호문의 평문을 구하는 문제이다.
평문 : 암호문의 반대이다. 즉, 두 번째 키를 만든 규칙을 찾아 반대로 적용하면 된다.

풀이 과정
1. 입력을 잘 받는다. (n : 한 문장의 단어 수, first_key : 첫 번째 키, second_key : 두 번째 키, secret_key : 암호문)
2. res 딕셔너리에 두 번째 키를 하나 씩 꺼내서 첫 번째 키의 해당 인덱스 값을 키로, 암호문의 첫 번째 글자가 값으로 만든다.
    - 이 방식이 두 번째 키를 만드는 규칙을 구하는 방식
3. res를 키로 정렬하고, 값들을 출력하면 된다.

위 풀이로 보면 설명이 부족한 거 같아 추가 (문제 예제 기준)
    첫 번째 키 : A B C D
    두 번째 키 : D A B C
    암호문    : C B A P

    'D'의 위치는 첫 번째 키의 3번째 인덱스
    'A'의 위치는 첫 번째 키의 0번째 인덱스
                .
                .
    즉, 두 번째 키를 기준으로 첫 번재 키의 인덱스 값들은 다음과 같이 된다.
    3, 0, 1, 2 -> 이 순서대로 암호문의 위치를 바꾸면 된다.
    'C'는 세 번째 인덱스로, 'B'는 0번째 인덱스, ... 이런 식으로 답을 구하면 B A P C 가 된다.

in
    2
    4
    A B C D
    D A B C
    C B A P
    3
    SECURITY THROUGH OBSCURITY
    OBSCURITY THROUGH SECURITY
    TOMORROW ATTACK WE
out
    B A P C
    WE ATTACK TOMORROW
'''

t = int(input())
for _ in range(t):
    n = int(input())
    first_key = list(input().split()) # 중복이 제거된 단어들
    second_key = list(input().split()) # 첫 번째 키의 단어들을 재배치해서 만들어 진 값
    secret_key = list(input().split()) # 평문을 두 번째 키를 만든 규칙의 반대로 재배치

    res = dict()
    for i in second_key:
        res[first_key.index(i)] = secret_key.pop(0)

    print(*[j for i, j in sorted(res.items())])
