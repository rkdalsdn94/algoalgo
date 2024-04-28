# 백준 - 실버3 - 숫자 야구 - 2503 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

완전 탐색 방식으로 123 ~ 987 까지 답을 찾아야 한다.

풀이 과정
 1. n과 n_list를 입력을 받는다.
 2. 123 ~ 987 까지 반복문을 돌려서 ck 함수로 체크한다.
 3. ck 함수를 만들어서 스트라이크와 볼을 체크한다. 체크하는 방식은 다음과 같다.
    3.1. 123 ~ 987 까지의 숫자를 문자열로 바꾼다. 해당 문자열이 n_list(스트라이크와 볼을 받는 리스트)의 값과 비교한다.
    3.2. 스트라이크와 볼이 맞지 않으면 False를 반환한다.
    3.3. 스트라이크와 볼이 맞으면 True를 반환한다.
 4. res 를 출력한다.
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 4
# n_list = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]] # 2

res = 0

def ck(num, q, s, b):
    q = list(str(q))

    strike = 0
    for i in range(3):
        if q[i] == num[i]:
            strike += 1

    if strike != s:
        return False

    ball = 0
    for i in range(3):
        if q[i] in num:
            ball += 1

    if ball - strike != b:
        return False
    return True

for i in range(123, 988):
    num = list(str(i))
    if num[0] == num[1] or num[1] == num[2] or num[0] == num[2] or '0' in num:
        continue

    flag = True
    for question, s, b in n_list:
        if not ck(num, question, s, b):
            flag = False
            break

    if flag:
        res += 1

print(res)
