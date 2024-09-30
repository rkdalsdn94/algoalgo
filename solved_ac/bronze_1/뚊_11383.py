# 백준 - 브론즈1 - 뚊 - 11383 - 구현, 문자열 문제
'''
구현, 문자열 문제

단순히 문자열을 비교하는 구현, 문자열 문제이다.

풀이 과정
    1. n, m을 입력받는다.
    2. arr와 arr2를 입력받는다.
    3. arr와 arr2를 순회하며 arr의 각 문자가 arr2의 문자 2개와 같은지 확인한다.
    4. 같지 않다면 Not Eyfa를 출력하고 종료한다.
    5. 모두 같다면 Eyfa를 출력한다.
'''

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
arr2 = [input() for _ in range(n)]

# 테스트
# n, m = 1, 5
# arr = ['ABCDE']
# arr2 = ['AABBCCDDEE'] # Eyfa
# n, m = 1, 5
# arr = ['ABCDE']
# arr2 = ['AABBCCDDEF'] # Not Eyfa
# n, m = 2, 2
# arr = ['AB', 'CD']
# arr2 = ['AABB', 'CCDD'] # Eyfa

for i in range(n):
    for j in range(m):
        if arr[i][j] * 2 != arr2[i][j * 2: j * 2 + 2]:
            print('Not Eyfa')
            exit()
print('Eyfa')
