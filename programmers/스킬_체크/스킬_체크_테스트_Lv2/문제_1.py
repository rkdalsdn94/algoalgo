# lcm 구하는 문제이다
from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def solution(arr):
    while len(arr) != 1:
        arr.append(lcm(arr.pop(), arr.pop()))
    
    return arr[0]

print(solution([2,6,8,14])) # 168
print(solution([1,2,3])) # 6