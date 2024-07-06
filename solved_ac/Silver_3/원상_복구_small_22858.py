# 백준 - 실버3 - 원상 복구 (small) - 22858 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

풀이 과정
    1. n, k를 입력받는다.
    2. s_list를 입력받는다.
    3. d_list를 입력받는다.
    4. k만큼 반복하면서
    5. temp를 n 만큼의 크기로 만들어 0으로 초기화한다.
    6. n만큼 반복하면서 temp[d_list[j] - 1]에 s_list[j]를 넣는다.
    7. s_list를 temp로 바꾼다.
    8. s_list를 출력한다.
'''

n, k = map(int, input().split())
s_list = list(map(int, input().split()))
d_list = list(map(int, input().split()))

# 테스트
# n, k = 5, 2
# s_list = [4, 1, 3, 5, 2]
# d_list = [4, 3, 1, 2, 5] # 1 4 5 3 2
# n, k = 4, 1
# s_list = [4, 3, 2, 1]
# d_list = [4, 3, 2, 1] # 1 2 3 4

for i in range(k):
    temp = [0] * n

    for j in range(n):
        temp[d_list[j] - 1] = s_list[j]
    
    s_list = temp

print(*s_list)
