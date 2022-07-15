'''
투 포인터 문제

변수를 두개(left, right) 사용해서 인덱스를 하나씩 옮겨가며
해당 인덱스 사이의 합이 a와 같은지 검사하면 된다.

while문 조건, left - right 수를 언제 움직이는지
위에 두 상황면 구하면 금방 풀 수 있다.
'''

# n, a = map(int, input().split())
# n_list = list(map(int, input().split()))

# 테스트
n, a = 4, 2
n_list = [1,1,1,1] # 3
n, a = 10, 5
n_list = [1,2,3,4,2,5,3,1,1,2] # 3
left, right = 0, 0

res = 0

while left <= right and right <= n:
    temp = sum(n_list[left:right])

    if temp == a:
        res += 1
        right += 1
    elif temp < a:
        right += 1
    else:
        left += 1

print(res)
