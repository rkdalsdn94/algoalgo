# 백준 - 실버4 - 양팔저울 - 25943 - 구현, 그리디 문제
'''
구현, 그리디 문제

문제에 있는 요구사항을 구현하고, 그리디하게 거스름돈(백준-5585 번) 문제 처럼 풀면 된다.

left 와 right 변수로 왼쪽 오른쪽의 값을 구한 후, temp 변수로 left right의 차를 절댓값으로 구한다.
그 다음 temp가 0이 아니면 무게 리스트에서 temp 가 0이 될 때까지 추를 올리면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 7
# n_list = [3,1,4,1,5,9,2] # 2
# n = 4
# n_list = [2,4,6,4] # 0
# n = 5
# n_list = [2,5,3,1,2] # 1

weight = [100, 50, 20, 10, 5, 2, 1]
res = 0
left, right = n_list[0], n_list[1]

for i in range(2, n):
    if left == right:
        left += n_list[i]
    elif left < right:
        left += n_list[i]
    else:
        right += n_list[i]

temp = abs(left - right)

if temp != 0:
    idx = 0

    while temp > 0:
        res += temp // weight[idx]
        temp %= weight[idx]
        idx += 1

print(res)
