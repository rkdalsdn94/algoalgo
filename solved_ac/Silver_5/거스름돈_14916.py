# 백준 - 거스름돈 - 실버5 - 14916 - dp 문제
'''
dp 문제

거스름돈이 n인 경우 최소 동전의 개수가 몇 개인지를 찾아야 되는 문제이다.
거스름돈은 2, 5 두 가지 동전 밖에 없어서 가장 큰 수로 나뉘는게 좋은 방법이여서
5로 나눴을 때 나머지가 0이면 해당 몫을 더해서 출력하면 된다.
나눠지지 않으면 - 2 씩 계속 하면서 해당 n이 음수가 되면 거슬러 줄 수 없는 상황이라
-1을 출력하고 종료하면 된다.
'''

# n = int(input())

# 테스트
n = 13 # 5
n = 14 # 4

res = 0

while 1:
    if n % 5 == 0:
        res += n // 5
        print(res)
        break
    else:
        n -= 2
        res += 1
    
    if n < 0:
        print(-1)
        break
