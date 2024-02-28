# 백준 - 브론즈2 - 24 - 1408 - 단순 구현, 사칙연산 문제
'''
단순 구현, 사칙연산 문제

풀이 과정
 - 주어진 입력 값에서 ':' 글자를 기준으로 split 한 뒤 계산하면 된다.
 - 초, 분, 시 기준으로 값을 계산하면 편하다.
    - 이때 시간의 값이 0보다 작으면 24에서 빼야 된다.
'''

a, b = input(), input()

# 테스트
# a, b = '13:52:30', '14:00:00'

new_a, new_b = list(map(int, a.split(':'))), list(map(int, b.split(':')))

hour = new_b[0] - new_a[0]
minute = new_b[1] - new_a[1]
second = new_b[2] - new_a[2]

if second < 0:
    minute -= 1
    second += 60

if minute < 0:
    hour -= 1
    minute += 60

if hour < 0:
    hour = 24 + hour

hour, minute, second = str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2)

print(hour + ':' + minute + ':' + second)
