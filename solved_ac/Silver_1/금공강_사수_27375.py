# 백준 - 실버1 - 금공강 사수 - 27375 - 완전 탐색, 백 트래킹 문제
'''
완전 탐색, 백 트래킹 문제

last_idx은 마지막으로 선택한 수업의 인덱스를 나타내며, 선택한 수업 간의 시간 겹침 여부를 검사하는 데 사용
초기에는 아직 어떤 수업도 선택되지 않았기 때문에 -1로 설정하여, 아무 수업도 선택되지 않은 상태임을 뜻한다.
이후 last_idx이 유효한 수업 인덱스를 가질 때, 새로 선택할 수업이 현재 선택된 수업과 겹치는지 확인하는 데 사용한다.

풀이 과정
    1. n, k를 입력받는다.
    2. n_list를 입력받는다.
    3. n_list를 정렬한다.
    4. res를 0으로 초기화한다.
    5. back_tracking 함수를 선언한다.
        6. total이 k와 같으면 res에 1을 더하고 return한다.
        7. i가 idx부터 n까지 반복하면서
            8. 금요일 수업은 모두 무시한다.
            9. 같은 요일에 시간이 겹치면 무시한다.
            10. back_tracking(i + 1, total + n_list[i][2] - n_list[i][1] + 1, i)를 호출한다.
    11. back_tracking(0, 0, -1)를 호출한다.
    12. res를 출력한다.
'''

n, k = map(int, input().split())
n_list = sorted([list(map(int, input().split())) for _ in range(n)])

# 테스트
# n, k = 10, 15
# n_list = sorted([
#     [3, 4, 4], [3, 4, 9], [3, 6, 8], [1, 10, 10], [3, 2, 5],
#     [2, 6, 10], [5, 5, 5], [2, 5, 7], [3, 6, 10], [3, 1, 6]
# ]) # 1

res = 0

def back_tracking(idx, total, last_idx):
    global res

    if total == k:
        res += 1
        return

    for i in range(idx, n):
        if n_list[i][0] == 5: # 금요일 수업 모두 무시
            continue

        # 같은 요일에 시간이 겹치는 경우
        # 이전 선택된 수업(last_idx)의 끝 시간이 다음 수업의 시작 시간과 겹친다면, 해당 수업을 선택하지 않습니다
        if last_idx != -1 and n_list[last_idx][0] == n_list[i][0] and n_list[last_idx][2] >= n_list[i][1]:
            continue

        back_tracking(i + 1, total + n_list[i][2] - n_list[i][1] + 1, i)

back_tracking(0, 0, -1)
print(res)
