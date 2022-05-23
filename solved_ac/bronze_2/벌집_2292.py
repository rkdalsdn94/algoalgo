'''
수학 문제

처음에 문제를 보고 어떻게 풀어야 되나 고민을 하다
문제에 있는 사진(?)을 보면 규칙이 있다.
1 이후로 주위의 원이 6의 배수로 증가한다.
2번째 방의 마지막 수 = 1 + 6 * 1
3번째 방의 마지막 수 = 1 + 6 * 2
4번째 방의 마지막 수 = 1 + 6 * 3
    .
    .
    .
위와 같은 식으로 증가한다. 그래서 temp를 하나 두고,
res를 1씩 더하면서 6을 곱하고 res가 n보다 커지는 순간이 이웃하는 방에 온 것이다.
몇 번째인지 구해야 되는 문제이므로 res를 출력하면 된다.
'''

n = int(input())

# 테스트
# n = 13 # 3
# n = 58 # 5

res, temp = 1, 1

while temp < n:
    temp += 6 * res
    res += 1

print(res)
