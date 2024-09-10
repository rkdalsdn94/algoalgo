# 백준 - 골드3 - 세 용액 - 2473 - 정렬, 이진 탐색, 투 포인터 문제
'''
정렬, 이진 탐색, 투 포인터 문제

전에 풀었던 다음의 두 문제와 비슷하다.
 - 용액 (https://www.acmicpc.net/problem/2467)
 - 두 용액 (https://www.acmicpc.net/problem/2470)
단, 이 문제는 세 용액을 출력하는 부분이여서 0에 가까운 수를 찾기 위해 zero_approximation을 사용했다.
풀이는 이진 탐색을 이용해서 0에 가깝게 하기 위해 세 수를 더해가며 답을 찾으면 된다.

풀이 과정
    1. n을 입력받는다.
    2. n_list를 입력받는다.
    3. n_list를 오름차순으로 정렬한다.
    4. zero_num을 1e100으로 설정한다.
    5. temp를 n_list의 첫 번째 값으로 설정한다.
    6. left, right를 1, n - 1로 설정한다.
    7. n - 2만큼 반복한다.
        7.1. temp를 n_list[i]로 설정한다.
        7.2. left, right를 i + 1, n - 1로 설정한다.
        7.3. left가 right보다 작을 때까지 반복한다.
            7.3.1. current_num을 temp + n_list[left] + n_list[right]로 설정한다.
            7.3.2. current_num의 절댓값이 zero_num의 절댓값보다 작거나 같다면 res를 [temp, n_list[left], n_list[right]]로 설정하고 zero_num을 temp + n_list[left] + n_list[right]로 설정한다.
            7.3.3. current_num이 0보다 작다면 left을 1 증가시킨다.
            7.3.4. current_num이 0보다 크다면 right를 1 감소시킨다.
            7.3.5. current_num이 0이라면 res를 [temp, n_list[left], n_list[right]]로 설정하고 반복을 종료한다.
    8. res를 출력한다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 5
# n_list = sorted([-2, 6, -97, -6, 98]) # -97 -2 98
# n = 7
# n_list = sorted([-2, -3, -24, -6, 98, 100, 61]) # -6 -3 -2

zero_approximation = int(1e100)
temp = n_list[0]
left, right = 1, n - 1
res = []

for i in range(n - 2):
    temp = n_list[i]
    left, right = i + 1, n - 1

    while left < right:
        current_num = temp + n_list[left] + n_list[right]

        if abs(current_num) <= abs(zero_approximation):
            res = [temp, n_list[left], n_list[right]]
            zero_approximation = temp + n_list[left] + n_list[right]

        if current_num < 0:
            left += 1
        elif current_num > 0:
            right -= 1
        else:
            res = [temp, n_list[left], n_list[right]]
            break

print(*res)
