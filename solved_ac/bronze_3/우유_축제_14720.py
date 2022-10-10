# 백준 - 우유 축제 - 브론즈3 - 14720 - 구현, 그리디 문제
'''
단순 구현, 그리디 문제

1. 맨 처음에는 딸기우유를 한 팩 마신다.
2. 딸기우유를 한 팩 마신 후에는 초코우유를 한 팩 마신다.
3. 초코우유를 한 팩 마신 후에는 바나나우유를 한 팩 마신다.
4. 바나나우유를 한 팩 마신 후에는 딸기우유를 한 팩 마신다. 
위 순서만 잘 지키면 된다.

0: 딸기우유만 파는 가게
1: 초코우유만 파는 가게
2: 바나나우유만 파는 가게

위의 3경우 밖에 없으니까, res를 3으로 나눴을 때 나머지랑 n_list의 인덱스랑 맞을때 1씩 증가하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 7
# n_list = [0,1,2,0,1,2,0] # 7

res = 0

for i in range(n):
    if n_list[i] == res % 3:
        res += 1

print(res)
