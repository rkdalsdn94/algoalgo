'''
수학, 구현 문제

a진법으로 이루어진 m_list를 10진법으로 변환 후 b진법으로 변환한 다음에 출력하면 된다.
m_list가 각 자리수 별로 나온다하니까 temp를 이용해 각 자리수를 더한 10진법의 숫자를 만든 후
해당 숫자를 b진법으로 변환하면 된다.

아래 while문은 b진법으로 변환하는 방법이다.
b진법으로 각 자릿수를 구한 후 res에 담은 다음에 (reverse()를 꼭 해야된다!!!) 출력하면 된다.
'''

a, b = map(int, input().split())
m = int(input())
m_list = list(map(int, input().split())) # a진법으로 이루어진 숫자

# 테스트
# a, b = 17, 8
# m = 2
# m_list = [2, 16]

temp = 0
res = []

for i in range(m):
    temp += m_list[i] * ( a ** (m - i - 1) )

while temp:
    num = temp % b
    res.append(num)
    temp = temp // b
res.reverse()

print(*res)
