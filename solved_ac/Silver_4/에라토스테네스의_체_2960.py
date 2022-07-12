'''
구현, 수학 문제

1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

위의 순서를 그대로 구현하면 된다.
'''

n, k = map(int, input().split())

# 테스트
# n, k = 7, 3 # 6
# n, k = 15, 12 # 7
# n, k = 10, 7 # 9

ck = [1] * (n + 1)
flag = False
cnt = 0

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if ck[j]:
            ck[j] = 0
            cnt += 1

            if cnt == k:
                print(j)
                flag = True
                break
    if flag:
        break
