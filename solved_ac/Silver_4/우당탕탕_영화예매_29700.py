# 백준 - 실버4 - 우당탕탕 영화예매 - 29700 - 구현, 문자열, 완전 탐색, 누적 합, 슬라이딩 윈도우 문제
'''
구현, 문자열, 완전 탐색, 누적 합, 슬라이딩 윈도우 문전

다양하게 풀 수 있는 문제이다.
아래 코드는 완전 탐색을 위주로 풀었다.
나중에 누적 합 또는 슬라이딩 윈도우로 풀어보는 것도 좋을 것 같다.

풀이 과정
 1. n, m, k를 입력받는다.
 2. n_list에 n개의 문자열을 입력받는다.
 3. res를 0으로 초기화한다.
 4. n_list를 순회하면서 각 문자열을 순회한다.
 5. 각 문자열을 순회하면서 m - k + 1만큼 순회한다.
 6. 만약 i[j]가 1이라면 continue한다.
 7. 만약 i[j:j + k]가 '0' * k와 같다면 res에 1을 더한다.
 8. res를 출력한다.
'''

n, m, k = map(int, input().split())
n_list = [input() for _ in range(n)]

# 테스트
# n, m, k = 3, 5, 3
# n_list = ['11000', '01010', '10000'] # 3
# n, m, k = 3, 4, 3
# n_list = ['1101', '1001', '0101'] # 0

res = 0

for i in n_list:
    for j in range(m - k + 1):
        if i[j:j + k] == '0' * k:
            res += 1

print(res)
