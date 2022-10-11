# 백준 - 사과 담기 게임 - 실버5 - 2828 - 구현, 그리디 문제
'''
구현, 그리디 문제

문제에 주어진 양식대로 입력을 다 받은 후 무제를 풀었다.
사과가 바구니가 있는 위치게 떨어진다면 그 턴은 건너 뛴다. (if left <= i and right >= i)
사과가 왼쪽에서 가깝다면 (left > i)
 - left에서 떨어지는 위치 i (apple_list) 를 빼준 값을 res에 더한다.
 - 왼쪽으로 움직인 만큼 right 값을 빼야된다.
오른쪽에 가깝다면 (else)
 - 왼쪽에 떨어진거 반대로 하면 된다.
'''

n, m = map(int, input().split())
j = int(input())
apple_list = [ int(input()) for _ in range(j) ]

# 테스트
# n, m = 5, 1
# j = 3
# apple_list = [1,5,3] # 6
# n, m = 5, 2
# j = 3
# apple_list = [1,5,3] # 4

res = 0
left = 1
right = m

for i in apple_list:
    if left <= i and right >= i:
        continue
    elif left > i:
        res += left - i
        right -= left - i
        left = i
    else:
        res += i - right
        left += i - right
        right = i

print(res)
