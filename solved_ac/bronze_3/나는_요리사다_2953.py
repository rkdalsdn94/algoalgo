# 백준 - 브론즈3 - 나는 요리사다 - 2953 - 단순 구현, 수학, 사칙연산 문제
'''
단순 구현, 수학, 사칙연산 문제

5번의 입력으로 들어오는 값 중에서 모두 더했을 때 합이 제일 큰 인덱스와, 그 값을 출력하면 되는 단순한 구현 문제이다.
합을 구하는 방법은 sum 함수를 사용했다.
'''

idx, res = 0, 0
for i in range(5):
    temp = sum(list(map(int, input().split())))

    if temp > res:
        res = temp
        idx = i + 1

print(idx, res)
