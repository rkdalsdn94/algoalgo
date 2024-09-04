# 백준 - 골드5 - 공약수 - 2436 - 수학, 완전 탐색, 정수론, 유클리드 호제법 문제
'''
수학, 완전 탐색, 정수론, 유클리드 호제법 문제

수학적인 지식이 필요한 문제이다. 다음의 블로그를 참고하면 좋다.
  - https://c4u-rdav.tistory.com/72

풀이 과정
    1. 입력을 받는다.
    2. div를 만들어서 lcm_num을 gcd_num으로 나눈 값을 넣는다.
    3. sqrt(div)까지 반복문을 돌면서 다음을 확인한다.
        3.1. div를 i로 나누었을 때 나머지가 0이고, gcd(i, div // i)가 1이면 다음을 수행한다.
            3.1.1. temp에 i * gcd_num과 div // i * gcd_num의 합을 넣는다.
            3.1.2. temp이 res의 합보다 작으면 res를 temp으로 바꾼다.
    4. res를 출력한다.
'''

from math import gcd, lcm, sqrt

gcd_num, lcm_num = map(int, input().split())

# 테스트
# gcd_num, lcm_num = 6, 180 # 30 36
# gcd_num, lcm_num = 2, 86486400 # 11648 14850

div = lcm_num // gcd_num
res = [int(1e9), int(1e9)]
temp = int(1e9)

for i in range(1, int(sqrt(div)) + 1):
    if div % i == 0 and gcd(i, div // i) == 1:
        temp = min(temp, sum([i * gcd_num, div // i * gcd_num]))

        if temp < sum(res):
            res = [i * gcd_num, div // i * gcd_num]

print(*res)
