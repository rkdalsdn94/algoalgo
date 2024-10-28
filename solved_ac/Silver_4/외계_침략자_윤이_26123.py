# 백준 - 실버4 - 외계 침략자 윤이 - 26123 - 구현 문제
'''
구현 문제

bisect에 대한 GPT 설명
  - Python의 bisect 모듈은 정렬된 리스트에서 효율적으로 값을 삽입하거나 특정 위치를 찾을 수 있도록 도와주는 함수들을 제공
  - bisect 모듈을 사용하면 이진 탐색(Binary Search)을 통해 정렬된 리스트를 다룰 수 있어 O(log N)의 시간 복잡도로 빠르게 위치를 찾을 수 있음
  - 주요 함수로는 bisect.bisect_left(), bisect.bisect_right()가 있음
    - bisect_left(a, x, lo=0, hi=len(a)) -> right는 반대로 생각하면 됨
        - 리스트 a에서 값 x를 삽입할 가장 왼쪽 위치를 반환한다.

풀이 과정
    1. n, d를 입력받는다.
    2. n_list를 입력받는다.
    3. n_list를 정렬한다.
    4. res를 0으로 초기화한다.
    5. current_height를 n_list의 마지막 원소로 초기화한다.
    6. current_height가 0이면 0을 출력하고 종료한다.
    7. d만큼 반복한다.
        8. idx에 bisect_left(n_list, current_height)를 저장한다.
        9. res에 n_list의 길이에서 idx를 뺀 값을 더한다.
        10. current_height를 1 감소시킨다.
        11. current_height가 0이면 종료한다.
    12. res를 출력한다.
'''

import bisect

n, d = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, d = 5, 3
# n_list = sorted([1, 3, 2, 5, 4]) # 6
# n, d = 5, 2
# n_list = sorted([1, 1, 1, 1, 1]) # 5

res = 0
current_height = n_list[-1]

if current_height == 0: # 모든 빌딩의 높이가 0인 경우
    print(0)
    exit(0)

for _ in range(d):
    idx = bisect.bisect_left(n_list, current_height) # 현재 높이 이상인 첫 번째 빌딩의 인덱스
    res += len(n_list) - idx # 가장 높은 빌딩 레이저 발사 횟수 더하기
    current_height -= 1 # 빌딩 높이 낮추기

    if current_height == 0: # 빌딩 높이가 0이면 종료
        break

print(res)
