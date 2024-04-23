# 백준 - 실버1 - 인간 컴퓨터 상호작용 - 16139 - 누적 합 문제
'''
누적 합 문제

누적 합을 이용해 문자열이 몇 번 나오는지 구하면 된다.
알파벳 소문자만 주어지므로 누적 합으로 사용할 prefix_sum의 배열을 26으로 해두고, 그 사이에 나오는 구간까지 해당 글자가 몇 번 나오는지 구하면 된다.

PyPy3로 제출해야 된다.

풀이 과정
 1. 입력을 받고 누적 합을 구한다.
    1.1. 누적 합을 구할 때 알파벳의 인덱스를 이용해 해당 글자가 몇 번 나오는지 구한다.
        1.1.1 알파벳의 인덱스를 구할 때 ord()를 사용하면 된다.
        1.1.2 누적합의 배열을 알파벳의 글자 수와 문자열의 길이만큼 만들어야 된다.
    1.2. 누적 합을 구할 때 이전 인덱스의 값을 더해주면 된다.
 2. 쿼리를 받고 해당 구간에 해당하는 글자가 몇 번 나오는지 구한다.
'''

s = input()
q = int(input())
q_list = [list(input().split()) for _ in range(q)]

# 테스트
# s = 'seungjaehwang'
# q = 4
# q_list = [
#     list('a 0 5'.split()),
#     list('a 0 6'.split()),
#     list('a 6 10'.split()),
#     list('a 7 10'.split())
# ] # 0  \  1  \  2  \  1

prefix_sum = [[0] * 26 for _ in range(len(s))]
prefix_sum[0][ord(s[0]) - ord('a')] += 1

for i in range(1, len(s)):
    a = ord(s[i]) - ord('a')
    prefix_sum[i][a] += 1

    for j in range(26): # 이 전의 값들을 더하는 부분
        prefix_sum[i][j] += prefix_sum[i - 1][j]

for a, b, c in q_list:
    a = ord(a) - ord('a')
    b = int(b)
    c = int(c)

    if b == 0:
        print(prefix_sum[c][a])
    else:
        print(prefix_sum[c][a] - prefix_sum[b - 1][a])
