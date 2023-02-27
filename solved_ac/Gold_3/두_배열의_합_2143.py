# 백준 - 골드3 - 두 배열의 합 - 2143 - 이진 탐색, 누적 합 문제
'''
이진 탐색, 누적 합 문제

누적 합에 대한 고민 때문에 결국 다른 사람의 풀이를 참고 했다. -> (코드는 안보고 풀이만 참고)
누적 합을 list에 미리 구해놓고 bisect를 이용해 이진 탐색으로 풀면 된다.

t = a_list[n] + b_list[n]
ㄴ> 즉, t - a_list[n] = b_list[n] 이다.
bisect_list를 통해 lower_bound(start), upper_bound(end)를 구한 다음
upper_bound(end) - lower_bound(start)의 차를 res에 더해가면서 답을 구하면 된다.

아래에 처음 누적 합의 힌트를 얻은 링크를 적어놨다. 설명도 되게 잘 되어 있어서 이해하기 훨씬 좋을거 같다.
(다 풀고 보니까 list를 다루는 것만 다르고 풀이는 똑같다. 다른 사람의 풀이를 봐도 거의 비슷하게 푼거 같다.)
https://imksh.com/78 --> 설명이 매우 잘 되어 있다.
'''

from bisect import bisect_left, bisect_right

t = int(input())
a, a_list = int(input()), list(map(int, input().split()))
b, b_list = int(input()), list(map(int, input().split()))

# 테스트
# t = 5
# a, a_list = 4, [1,3,1,2]
# b, b_list = 3, [1,3,2] # 7

res = 0

for i in range(a): # a_list의 누적 합 미리 구하기
    for j in range(i + 1, a):
        a_list.append(sum(a_list[i:j + 1]))

for i in range(b): # b_list의 누적 합 미리 구하기
    for j in range(i + 1, b):
        b_list.append(sum(b_list[i:j + 1]))
a_list.sort(); b_list.sort() # 이진 탐색을 위한 정렬

for i in a_list: # t = a_list[n] + b_list[n] --> 즉, t - a_list[n] = b_list[n] 이다.
    lower_bound = bisect_left(b_list, t - i)
    upper_bound = bisect_right(b_list, t - i)
    res += upper_bound - lower_bound

print(res)
