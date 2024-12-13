# 백준 - 브론즈1 - 배고파 Easy - 28239 - 수학, 완전 탐색, 비트 마스킹 문제
'''
수학, 완전 탐색, 비트 마스킹 문제

입력받은 n을 이진수로 변환하고, 1의 개수를 세는 문제이다.

풀이 과정
    1. n을 입력받는다.
    2. n을 이진수로 변환한다.
    3. 이진수에서 1의 개수를 센다.
    4. 1이 하나만 있는 경우
        - 해당 비트의 위치를 찾아서 그보다 1 작은 값을 두 번 출력
    5. 1이 여러 개인 경우
        - 모든 1의 위치를 출력
'''

n = int(input())
m_list = [int(input()) for _ in range(n)]

# 테스트
# n = 3
# m_list = [10, 3] # 1 3  \  0 1

for m in m_list:
    # 이진수로 변환하고 '0b' 접두사 제거
    binary = bin(m)[2:]

    # 1의 개수 세기
    ones_count = binary.count('1')

    if ones_count == 1:
        # 1이 하나만 있는 경우
        # 해당 비트의 위치를 찾아서 그보다 1 작은 값을 두 번 출력
        position = len(binary) - binary.rfind('1') - 1
        print(f'{position - 1} {position - 1}')
    else:
        # 1이 여러 개인 경우
        # 모든 1의 위치를 출력
        positions = []
        for i in range(len(binary)):
            if binary[len(binary) - 1 - i] == '1':
                positions.append(str(i))
        print(' '.join(positions))
