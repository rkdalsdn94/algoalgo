# 백준 - 골드4 - 꿀 따기 - 21758 - 그리디, 누적 합, 많은 조건 분기 문제
'''
그리디, 누적 합, 많은 조건 분기 문제

다음 영상의 설명을 참고해서 풀 수 있었다.
https://www.youtube.com/watch?v=gOZjIAplync&t=510s

100점을 맞기 위해선 구간 합을 사용해야 한다.

풀이 방식은 다음과 같다.
prefix_sum 이라는 이름의 구간 합 변수를 구해둔 뒤 벌통의 위치를 수정해가며 풀면 된다.

벌통의 위치를 '중앙', '오른쪽', '왼쪽' 을 둔다는 가정을 하고 풀었다.
    벌통의 위치를 '중앙'이라고 할 때 벌의 위치는 양 끝을 고정시키고, 벌통의 위치를 바꿔가며 구한다 단, 벌은 양 끝으로 고정시켜야 한다.
    이유는 양 끝에 아무리 큰 값이 벌통이 중앙에 있을 때 먹을 수 있는 방법이 없다.
    따라서, 벌통이 '중앙'에 위치했을 경우에는 양 끝으로 벌을 고정시켜야 되고, 구간 합을 통해 구하는 방식은 다음과 같다.
    prefix_sum 에서 n - 1 값에서 첫 번째 값을 빼고(벌의 양 끝이므로 획득할 수 없는 꿀),
    벌통이 존재하는 i를 한번 더 더해줘야 한다.(양 쪽에서 두 벌이 같이 획득할 수 있으므로)

    벌통의 위치가 '오른쪽' 일 때는 벌의 위치를 수정시켜야 한다.
    구간 합을 통해 구한 값으로 벌의 위치를 수정하며 구하면 되고,
    '왼쪽' 일 때도 위와 같이 풀면 된다.

코드를 봐도 이해가 어려문 위에 참고해놓은 영상을 보면 쉽게 이애할 수 있다.
'''

n = int(input())
n_list = [0] + list(map(int, input().split()))

# 테스트
# n = 7
# n_list = [0] + [9, 9, 4, 1, 4, 9, 9] # 57
# n = 7
# n_list = [0] + [4, 4, 9, 1, 9, 4, 4] # 54
# n = 3
# n_list = [0] + [2, 5, 4] # 10

prefix_sum = [0] * (n + 1)
res = 0

for i in range(1, n + 1):
    prefix_sum[i] = n_list[i] + prefix_sum[i - 1]

for i in range(2, n):
    # 벌통이 중앙
    res = max(res, prefix_sum[n - 1] - n_list[1] + n_list[i])

    # 벌통이 오른쪽
    res = max(res, (prefix_sum[n] - n_list[1] - n_list[i]) + (prefix_sum[n] - prefix_sum[i]))

    # 벌통이 왼쪽
    res = max(res, (prefix_sum[n - 1] - n_list[i]) + prefix_sum[i - 1])

print(res)
