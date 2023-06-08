# 백준 - 실버4 - 링 - 3036 - 수학, 정수론, 유클리드 호제법 문제
'''
수학, 정수론, 유클리드 호제법 문제

gcd를 구한 후 n_list[0]를 분자로 현재 반복중인 n_list[i]를 분모로 나눴을 때 몫을 출력하면 된다.
실제 gcd를 구해도 되지만, python 내장 모듈인 math 에서 gcd를 사용해도 된다.
직접 gcd를 구한 부분은 파일 제일 아래에 있다.
'''

from math import gcd

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 3
# n_list = [8, 4, 2] # 2/1    4/1
# n = 4
# n_list = [12, 3, 8, 4] # 4/1    3/2    3/1
# n = 4
# n_list = [300, 1, 1, 300] # 300/1    300/1    1/1

for i in range(1, n):
    gcd_num = gcd(n_list[0], n_list[i])
    print(f'{n_list[0] // gcd_num}/{n_list[i] // gcd_num}')


'''
직접 gcd 구하기

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
'''
