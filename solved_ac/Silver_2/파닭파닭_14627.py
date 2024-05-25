# 백준 - 실버2 - 파닭파닭 - 14627 - 이진 탐색, 매개 변수 탐색 문제
'''
이진 탐색, 매개 변수 탐색 문제

이진 탐색 후 해당 결과를 c로 곱한 뒤 s_list의 합에서 빼면 된다.
PyPy3로 제출하거나 input을 sys.stdin.readline으로 받아야 된다.

풀이 과정
 1. 입력을 받고, s_list를 입력받는다.
 2. 이진 탐색을 이용하여 최대값을 찾는다.
    2.1. start와 end를 설정하고, mid를 계산한다.
    2.2. cnt를 0으로 초기화하고, s_list를 돌면서 mid로 나눈 몫을 cnt에 더한다.
    2.3. cnt가 c보다 크거나 같은 경우 start를 mid + 1로 설정하고, res와 mid 중 큰 값을 res에 저장한다.
    2.4. cnt가 c보다 작은 경우 end를 mid - 1로 설정한다.
 3. 출력할 때는 s_list의 합에서 res * c를 뺀 값을 출력해야 된다.
'''

s, c = map(int, input().split())
s_list = [int(input()) for _ in range(s)]

# 테스트
# s, c = 3, 5
# s_list = [440, 350, 230] # 145

start, end = 1, max(s_list)
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum([i // mid for i in s_list])

    if cnt >= c:
        start = mid + 1
        res = max(res, mid)
    else:
        end = mid - 1

print(sum(s_list) - res * c)
