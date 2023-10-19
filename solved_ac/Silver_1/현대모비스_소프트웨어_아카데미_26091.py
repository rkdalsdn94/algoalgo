# 백준 - 실버1 - 현대모비스 소프트웨어 아카데미 - 26091 - 정렬, 투 포인터 문제
'''
정렬, 투 포인터 문제

문제에서 주어진 두 조건만 체크하면 된다.
- 팀원이 두 명이다.
- 팀의 능력치가 M 이상이다. 팀의 능력치는 모든 팀원의 능력치를 합한 값이다.

난이도의 비해 크게 어렵지 않다.
입력으로 주어지는 팀의 능력치(n_list)를 정렬한 다음, 투 포인터를 활용하면 된다.

풀이 과정
1. 투 포인터를 사용하기 위한 left와 right를 각각 0과 n - 1로 초기화한다.
2. 두 팀원의 능력치를 더하기 위해 n_list[left], n_list[right] 두 능력치를 더한다.
3. 더한 능력치(temp)가 m보다 크거나 같으면
    3.1 res와 left를 각각 1씩 더하고, right는 1을 뺀다.
4. 작으면 left만 1 증가시킨다. (정렬되어 있기 때문, m보다 크거나 같은 상황을 만들기 위해)

while 조건으로는 팀원이 두 명이여야 되기 때문에 left가 right보다 작을 때까지만 반복해야 한다.
'''

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, m = 6, 10
# n_list = sorted([3, 5, 7, 3, 5, 6]) # 2
# n, m = 1, 10
# n_list = sorted([100]) # 0

left, right = 0, n - 1
res = 0

while left < right:
    temp = n_list[left] + n_list[right]

    if temp >= m:
        res += 1
        right -= 1
        left += 1
    else:
        left += 1

print(res)
