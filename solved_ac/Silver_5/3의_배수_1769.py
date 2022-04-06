'''
구현, 문자열, 재귀 문제
재귀는 사용하지 않았다. (반복문을 재귀로 만들면 될거 같은데 while문이 더 빠르게 동작할 거 같다.)

문제에 주어진 대로 문자열의 len이 1이 될 때까지 반복문을 돌린 후 sum(list(map(int, x)))
res를 1씩 더해 준 후 len이 1이 됐을 때, 반복문을 하고
3의 자리 인지 계산 후 출력한다.
'''

# x = input()

# 테스트
x = '1234567' # 3 \n NO

res = 0

while len(x) != 1:
    x = str(sum(list(map(int, x))))
    res += 1

print(res)
if int(x) % 3 == 0: print('YES')
else: print('NO')
