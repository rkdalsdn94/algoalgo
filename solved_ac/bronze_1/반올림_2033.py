# 백준 - 브론즈1 - 반올림 - 2033 - 수학, 구현 문제
'''
수학, 구현 문제

풀이 과정
 - temp 10으로 만들어 놓고, n이 temp보다 크면 while 문으로 반복을 실행한다.
 - 반복문 내에서 n을 temp로 나눈 나머지가 temp를 2로 나눈 몫보다 크다면(반올림 조건)
    - temp를 n에 더해준다.
 - 위 과정을 진행한 후 0으로 맞추기 위해 n에서 n을 temp로 나눈 나머지를 빼고, temp에 10을 곱한다.
 - while 문이 끝났을 때 n을 출력하면 된다.
'''

n = int(input())

# 테스트
# n = 15 # 20
# n = 446 # 500

temp = 10

while n > temp:
    if n % temp >= temp // 2:
        n += temp

    n -= (n % temp)
    temp *= 10

print(n)
