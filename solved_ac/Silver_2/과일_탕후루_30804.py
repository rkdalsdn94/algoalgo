# 백준 - 실버2 - 과일 탕후루 - 30804 - 구현, 완전 탐색, 투 포인터 문제
'''
구현, 완전 탐색, 투 포인터 문제

각 과일 개수를 세야되므로 딕셔너리를 사용했다.

풀이 과정
    1. 딕셔너리를 사용하여 각 과일 개수를 센다.
    2. 투 포인터를 사용하여 완전 탐색을 진행한다.
    3. 왼쪽 포인터가 오른쪽 포인터보다 작은 경우 반복문을 돌린다.
    4. 딕셔너리에 있는 과일 개수가 0이 되면 해당 과일을 삭제한다.
    5. 결과 출력
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [5, 1, 1, 2, 1] # 4
# n = 3
# n_list = [1, 1, 1] # 3
# n = 9
# n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 2

res = 0
left, right, temp = 0, 0, 0
cnt = {}

while right < n:
    if n_list[right] in cnt:
        cnt[n_list[right]] += 1
    else:
        cnt[n_list[right]] = 1
        temp += 1

    while temp > 2:
        cnt[n_list[left]] -= 1

        if cnt[n_list[left]] == 0:
            del cnt[n_list[left]]
            temp -= 1
        left += 1

    res = max(res, right - left + 1)
    right += 1

print(res)
