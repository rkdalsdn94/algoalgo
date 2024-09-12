# 백준 - 실버4 - Fishmongers - 17906 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

정렬과 그리디하게 1키로 무게당 가격이 가장 높은 물고기를 팔면 된다.
그래서 fish_mongers의 가격이 높은 순서대로 정렬하고 fish_weight_list를 내림차순으로 정렬한다.
그리고 fish_mongers를 돌면서 물고기를 팔면 된다.
while 문 내에서 fish_weight_index를 검사하는 부분이 없으면 indexError가 나온다.

풀이 과정
    1. n, m을 입력받는다.
    2. fish_weight_list를 입력받는다.
    3. fish_mongers를 입력받는다.
    4. fish_weight_list를 내림차순으로 정렬한다.
    5. fish_mongers를 가격이 높은 순서대로 정렬한다.
    6. res를 0으로 초기화한다.
    7. fish_weight_index를 0으로 초기화한다.
    8. fish_mongers를 돌면서 다음을 확인한다.
        8.1. fish_count, fish_amount를 i, j로 받는다.
        8.2. fish_count가 0보다 크고 fish_weight_index가 n보다 작다면 다음을 반복한다.
            8.2.1. res에 fish_amount * fish_weight_list[fish_weight_index]를 더한다.
            8.2.2. fish_weight_index를 1 증가시킨다.
            8.2.3. fish_count를 1 감소시킨다.
    9. res를 출력한다.
'''

n, m = map(int, input().split())
fish_weight_list = sorted(list(map(int, input().split())), reverse=True)
fish_mongers = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[1], reverse=True)

# 테스트
# n, m = 4, 3
# fish_weight_list = sorted([1, 2, 7, 5], reverse=True)
# fish_mongers = sorted([[2, 4], [1, 5], [3, 3]], key=lambda x: x[1], reverse=True) # 66

res = 0
fish_weight_index = 0

for i, j in fish_mongers:
    fish_count, fish_amount = i, j

    while fish_count > 0 and fish_weight_index < n:
        res += fish_amount * fish_weight_list[fish_weight_index]
        fish_weight_index += 1
        fish_count -= 1

print(res)
