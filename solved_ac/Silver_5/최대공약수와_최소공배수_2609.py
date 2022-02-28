'''
# from math import lcm, gcd
# a, b = map(int, input().split())
# print(gcd(a, b))
# print(lcm(a, b))
위에 4줄로도 코드를 완성 시킬 수 있다.
대신 python의 버전이 3.9 이상에서만 lcm이 import 가능하다 (현재(2022-02-28) 백준의 버전은 3.10.x이라서 위에 4줄로 통과가 가능하다)

모듈을 사용하지 않고 만드려면 유클리드 호제법을 사용하는 방식이 가장 좋다.
유클리드 호제법을 잘 모르면 https://tech.lonpeach.com/2017/11/12/Euclidean-algorithm/ 여기 블로그를 참고하면 좋다
'''


a, b = map(int, input().split())

# 테스트
# a, b = 24, 18 # 6 \n 72

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))
