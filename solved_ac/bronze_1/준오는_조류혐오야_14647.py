# 백준 - 브론즈1 - 준오는 조류혐오야 - 14647 - 구현, 문자열 문제
'''
구현, 문자열 문제

19% 에서 틀렸다면 열을 검사해보자. (이 부분을 신경쓰지 못 해 틀렸다.)

풀이 과정
 1. 입력을 받고, n_list를 만든다.
 2. total_nine에 n_list의 모든 원소에서 '9'의 개수를 더한다.
 3. n_list의 행을 기준으로 ''.join 한 뒤 '9'의 개수를 센 뒤 row_max에 저장한다.
 4. n_list의 열을 행으로 변환한다.
 5. n_list의 열을 기준으로 ''.join 한 뒤 '9'의 개수를 센 뒤 col_max에 저장한다.
 6. total_nine에서 row_max와 col_max 중 큰 값을 뺀 값을 출력한다.
'''

n, m = map(int, input().split())
n_list = [list(input().split()) for _ in range(n)]

# 테스트
# n, m = 3, 4
# n_list = [
#     ['1', '2', '3', '9'], ['4', '5', '9', '6'], ['9', '7', '8', '9']
# ] # 2
# n, m = 3, 4
# n_list = [
#     ['11', '12', '19', '14'], ['99', '39', '14', '90'], ['13', '47', '81', '99'], ['32', '72', '29', '66']
# ] # 4

row_max, col_max = 0, 0
total_nine = 0

for i in n_list:
    total_nine += ''.join(i).count('9')

# row 검사
for i in range(n):
    temp = ''.join(n_list[i]).count('9')

    if temp >= row_max:
        row_max = temp

n_list = list(map(list, zip(*n_list))) # 열을 행으로 변환 (세로 줄을 가로 줄로 변환)

# col 검사
for i in range(m):
    temp = ''.join(n_list[i]).count('9')

    if temp >= col_max:
        col_max = temp

print(total_nine - max(row_max, col_max))
