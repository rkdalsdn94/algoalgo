# 백준 - 브론즈1 - 비밀 이메일 - 2999 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
 - 약수를 이용해 r과 c를 구해야 된다.
    - 약수가 짝수면 중간 위치의 값 2개, 홀수면 중간 값 1개가 r, c가 괸다.
 - 이 후 입력으로 들어온 문자열을 재배치한 뒤 출력하면 된다.
'''

word = input()

# 테스트
# word = 'bok' # bok
# word = 'koaski' # kakosi
# word = 'boudonuimilcbsai' # bombonisuuladici

# 약수 구하기
divisor = []
for i in range(1, len(word) + 1):
    if len(word) % i == 0:
        divisor.append(i)

# 약수를 통해 r과 c 구하기
if len(divisor) % 2 == 0:
    r = divisor[len(divisor) // 2 - 1]
    c = divisor[len(divisor) // 2]
else:
    r = c = divisor[len(divisor) // 2]

res = [[0] * c for _ in range(r)]
temp_idx = 0

for i in range(c):
    for j in range(r):
        res[j][i] = word[temp_idx]
        temp_idx += 1

for i in res:
    print(''.join(i), end='')
