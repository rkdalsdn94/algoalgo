# 백준 - 실버1 - 하노이 탑 - 1914 - 재귀 문제
'''
재귀 문제

하노이 탑 관련 자료들이 많아 따로 풀이를 적지 않고, 아래 영상으로 보면 이해가 잘 된다.
    - https://www.youtube.com/watch?v=FYCGV6F1NuY

n이 20보다 작을 경우에만 이동하는 방향을 출력하면 된다.
'''

n = int(input())

# 테스트
# n = 3

def hanoi(n, start, end, mid):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, mid, end)
    print(start, end)
    hanoi(n - 1, mid, end, start)

print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3, 2)
