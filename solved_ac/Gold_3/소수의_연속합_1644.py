# 백준 - 골드3 - 소수의 연속합 - 1644 - 투 포인터, 에라토스테네스의 체 문제
'''
투 포인터, 에라토스테네스의 체 문제

풀이 과정
1. 에라토스테네스의 체를 이용해서 n 까지의 소수를 구한다.
2. 위에서 구한 소수 리스트로 투 포인터를 통해 연속합이 n이 됐을 때 res를 1씩 더한다.
    2.1 left, right를 각각 0, 1로 설정한 뒤, n보다 작으면 right를 증가시키고, 크면 left를 증가시킨다.
    2.2 n이랑 같다면 right와 res를 증가시킨다.
    2.3 위 과정을 right가 소수 리스트 길이보다 작거나 같을 때까지 반복한다.

아래와 같이 풀었는데, sum 함수 때문에 그런지 시간이 오래 걸렸다.
시간을 줄이려면 sum을 사용하지 않고, temp에 prime_num_list 값을 더하거나 빼면서 시간을 좀 더 줄일 수 있다.
'''

n = int(input())

# 테스트
# n = 20 # 0
# n = 3 # 1
# n = 41 # 3
# n = 53 # 2

sieve_of_eratosthenes = [0, 0] + [1] * (n + 1)
prime_num_list = []
left, right = 0, 1
res = 0

# 소수 리스트 구하기
for i in range(2, n + 1):
    if sieve_of_eratosthenes[i]:
        prime_num_list.append(i)
        for j in (i * 2, n + 1, i):
            prime_num_list[j] = 0

while right <= len(prime_num_list):
    temp = sum(prime_num_list[left:right])

    if temp == n:
        res += 1
        right += 1
        left += 1
    elif temp < n:
        right += 1
    else:
        left += 1

print(res)
