# 백준 - 브론즈1 - 암호 - 1855 - 구현, 문자열 문제
'''
구현, 문자열 문제

'왼쪽 → 오른쪽, 오른쪽 → 왼쪽, 왼쪽 → 오른쪽' 이 부분을 신경쓰고 풀어야 되는 문제이다.
입력으로 들어온 문자열을 k(열의 개수)로 자른 후, 두 번째 실행때마다 역순으로 담아야 된다.

그 후에 세로줄로 한 글자씩 res에 추가한 뒤 출력하면 된다.
'''

k = int(input())
password = input()

# 테스트
# k = 3
# password = 'aeijfbcgklhd' # abcdefghijkl

temp_list = []
res = ''
temp_cnt = 0

for i in range(0, len(password), k):
    if temp_cnt % 2 == 0:
        temp_list.append(password[i : i + k])
    else:
        temp_list.append(password[i : i + k][::-1])
    temp_cnt += 1

for i in range(len(temp_list[0])):
    for j in range(len(temp_list)):
        res += temp_list[j][i]

print(res)