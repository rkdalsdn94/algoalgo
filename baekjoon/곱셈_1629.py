# a,b,c = map(int, input().split())
# a,b,c = 10, 11, 12
# print(pow(a,b,c))

# 처음에 위에처럼 풀었다가 다른 사람 풀이에 재귀로 푸는 방식 있어서 가져옴
a,b,c = map(int, input().split())
# a,b,c = 10, 11, 12
def pow(a, b, c):
    if b==1:
        return a % c
    temp = pow(a, b//2, c)
    temp = temp * temp % c
    if b % 2 == 0:
        return temp
    return temp * a % c

print(pow(a,b,c))