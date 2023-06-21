# 백준 - 브론즈2 - 창영마을 - 3028 - 단순 구현, 문자열, 시뮬레이션 문제
'''
단순 구현, 문자열, 시뮬레이션 문제

단순하게 정답으로 출력할 res 배열에 컵을 뜻하는 의미로 3개의 원소를 담아둔다. (제일 왼쪽에 공이 있어서 0번째 인덱스에 1로 초기화한다.)
A, B, C 각각의 operation 마다 문제에 나와있듯이 인덱스를 수정하면 되는 간단한 구현 문제이다.

A : 0, 1 위치 바꾸기
B : 1, 2 위치 바꾸기
C : 0, 2 위치 바꾸기
'''

operation = input()

# 테스트
# command = 'AB' # 3
# command = 'CBABCACCC' # 1

res = [1,0,0]

for i in operation:
    if i == 'A':
        res[0], res[1] = res[1], res[0]
    elif i == 'B':
        res[1], res[2] = res[2], res[1]
    elif i == 'C':
        res[2], res[0] = res[0], res[2]

print(res.index(1) + 1)
