# 백준 - 두 수의 합 - 3273 - 실버3 - 정렬, 투 포인터 문제
'''
정렬, 투 포인터 문제

처음에 단순하게 생각해서 2중 for 문으로 구하려고 하다가 바로 시간 초과가 나왔다.
n의 범위를 생각하면 당연한 일이다..
그래서 문제를 다시 읽고 어떻게 풀어야 할지 고민하던 중
문제의 태그가 정렬, 투 포인터인 걸 보고 해당 방식으로 풀려고 한다.

n_list를 입력받고 정렬을 한 후, left, right 변수를 만들어 두 수의 합이 x가 됐을 때 res에 1을 더한다.
반복문은 left의 변수가 right 변수보다 같거나 크면 종료할 수 있게 while 문으로 실행시킨다.
마지막으로 res를 출력하면 된다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))
x = int(input())

# 테스트
# n = 9
# n_list = sorted([5, 12, 7, 10, 9, 1, 2, 3, 11])
# x = 13 # 3

left, right = 0, n - 1
res = 0

while left < right:
    temp = n_list[left] + n_list[right]

    if temp == x:
        res += 1
        left += 1
    elif temp > x:
        right -= 1
    else:
        left += 1

print(res)

'''
시간 초과 코드

n = int(input())
n_list = list(map(int, input().split()))
x = int(input())

res = 0

for i in range(n):
    for j in range(i, n):
        if n_list[i] + n_list[j] == x:
            res += 1
'''