# 백준 - 실버1 - 소수&팰린드롬 - 1747 - 수학, 완전 탐색, 에라토스테네스의 체
'''
수학, 완전 탐색, 에라토스테네스의 체

98 ~ 99% 에서 틀린다면 n이 1일 때 처리를 해야 된다.
나머지 풀이는 소수인지 체크하는 부분과 팰린드롬인지 체그하는 부분으로 구하면 되고,
둘 다 아닐 경우 될 때까지 완전 탐색 방식으로 n을 1씩 더하면 된다.
'''

n = int(input())

# 테스트
# n = 31 # 101

res = 0

def prime_check(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def palindrome_check(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

while 1:
    if prime_check(n) and palindrome_check(n):
        res = n
        break
    n += 1

print(res)
