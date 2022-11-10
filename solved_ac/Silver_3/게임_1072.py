# 백준 - 게임 - 실버3 - 1072 - 수학, 이분 탐색 문제
'''
수학, 이분 탐색 문제

이분 탐색으로 start와 end를 설정한 후 mid값을 1씩 더하고 빼면서 값을 찾아가면 된다.

풀이 과정
1. start(0)와 end(x, y 중 큰 값의 + 1)를 설정한다.
2. 두 값의 승률을 구해 z로 만든다. -> y * 100 // x
3. start가 end를 넘을때까지 while 반복문을 실행시킨다다
4. while문 안에서 mid(start + end // 2) 값을 설정하고 nz라는 변수로 승률이 변하는지 구한다.
5. while을 벗어나는 순간 end에 + 1 한 상태로 출력하고, 만약 처음 승률이 99퍼 이상이였다면 어차피 변하지 않을 승률이므로 -1을 출력한다.
'''

x, y = map(int, input().split())

# 테스트
# x, y = 10, 8 # 1
# x, y = 100, 80 # 6
# x, y = 47, 47 # -1
# x, y = 99000, 0 # 1000
# x, y = 1000000000, 470000000 # 19230770

start, end = 0, max(x, y) + 1
z = y * 100 // x

while start <= end:
    mid = (start + end) // 2
    nz = (y + mid) * 100 // (x + mid)

    if nz > z:
        end = mid - 1
    else:
        start = mid + 1

print(-1) if z >= 99 else print(end + 1)
