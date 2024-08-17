# 백준 - 실버5 - Jumbled Communication - 11675 - 구현, 완전 탐색, 비트마스킹 문제
'''
구현, 완전 탐색, 비트마스킹 문제

문제 해석을 잘 해야 된다. (문제 난이도가 높은 편은 아니지만 해석이 어렵다 언제쯤 번역기를 안 쓰고 풀 수 있을까...)
입력 부분만 보고도 어느정도 풀이를 유추할 수 있다.
    - one line with an integer n (1 ≤ n ≤ 10^5), the number of bytes in the message sent by the weather sensor;
    - one line with n integers b1, . . . , bn (0 ≤ bi ≤ 255 for all i), the byte values of the message.

풀이 과정
    1. 입력을 받는다.
    2. res를 만들어 값을 저장한다.
    3. 비트마스킹을 이용해 값을 구한다.
        3.1. (j ^ (j << 1) & 255 == n_list의 값) 조건을 만족하면 res에 추가하고, break한다.
    4. res를 출력한다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [58, 89, 205, 20, 198] # 22 55 187 12 66

res = []

for i in n_list:
    for j in range(256):
        if j ^ (j << 1) & 255 == i:
            res.append(j)
            break

print(*res)
