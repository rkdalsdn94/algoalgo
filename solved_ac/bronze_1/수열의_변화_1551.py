# 백준 - 브론즈1 - 수열의 변화 - 1551 - 단순 구현, 문자열, 시뮬레이션, 파싱 문제
'''
단순 구현, 문자열, 시뮬레이션, 파싱 문제

입력으로 들어오는 문자열열을 ','를 기준으로 파싱한 후 map 함수를 이용해 int 형으로 형변환을 변환 시킨다.
문제에 주어진 요구사항대로 A[i + 1] - A[i]를 temp라는 리스트에 담아둔 후 A를 temp 와 변경하고 k번 반복하면 된다.
단순한 구현, 시뮬레이션 문제이다.
'''

n, k = map(int, input().split())
A = list(map(int, input().split(',')))

# 테스트
# n, k = 5, 1
# A = list(map(int, '5,6,3,9,-1'.split(','))) # 1,-3,6,10
# n, k = 5, 2
# A = list(map(int, '5,6,3,9,-1'.split(','))) # -4,9,16
# n, k = 5, 4
# A = list(map(int, '5,6,3,9,-1'.split(','))) # -38
# n, k = 8, 3
# A = list(map(int, '4,4,4,4,4,4,4,4'.split(','))) # 0,0,0,0,0
# n, k = 2, 0
# A = list(map(int, '-100,100'.split(','))) # -100,100


for _ in range(k):
    temp = []

    for i in range(len(A) - 1):
        temp.append(A[i + 1] - A[i])
    A = temp

print(','.join(map(str, A)))
