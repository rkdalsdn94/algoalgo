# 백준 - 수들의 합 5 - 2018 - 수학, 투 포인터 문제
'''
수학, 투 포인터 문제

처음에 n의 범위까지 해당 리스트를 만든 다음에 풀려고 하다가 메모리 초과가 나왔다.
그래서 list를 사용하지 않고 int형으로 숫자를 더하고 빼고 하면서 푸니까 통과할 수 있었다.
근데 다른 사람들의 코드보다 시간은 오래 걸리게 푼거 같다.

푸는 방식은 투 포인터의 전형적인 문제이다.
start와 end를 초기화 시킨 후 해당 수드르이 합이 n이 되면 res를 더해준다.
합이 n보다 적을 땐 end의 수를 늘려 temp에 더하고, 크면 start를 더한 후 temp에서 수를 빼는 방식으로 풀었다.
'''

n = int(input())
start, end = 0, 0
temp, res = 0, 0

while end <= n:
    if temp < n:
        end += 1
        temp += end
    elif temp > n:
        start += 1
        temp -= start
    else:
        res += 1
        start += 1
        temp -= start

print(res)


''' 메모리 초과 코드
# n = int(input())

# 테스트
n = 10 # 2
n = 15 # 4

n_list = [ i for i in range(n + 1) ]
res = 0
start, end = 0, 1

while end <= n:
    temp = sum(n_list[start:end + 1])

    if temp == n:
        res += 1
        end += 1
    elif temp < n:
        end += 1
    else:
        start += 1

print(res)
'''