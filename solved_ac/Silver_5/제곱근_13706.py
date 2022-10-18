# 백준 - 제곱근 - 실버5 - 13706 - 수학, 이분 탐색 문제
'''
수학, 이분 탐색 문제

제곱근을 구하는 문제여서 꼼수로 파이썬 내장 함수인 math를 이용해서 풀려고 했는데 OverflowError 가 나왔다..
 - https://help.acmicpc.net/judge/rte/OverflowError -> OverflowError에 관한 백준 설명 링크
그래서, 이분 탐색으로 다시 풀었다.

풀이 과정
1. start와 end를 각각 0과 n으로 설정한 다음 두 수를 더하고 2로 나눈 몫을 mid 값으로 설정한다.
2. mid 값을 2로 제곱(temp) 한 다음 그 값이 n과 같다면 해당 mid 값 출력
    2.1 temp 값이 n보다 작다면 start 값 증가
    2.2 temp 값이 n보다 크다면 end 값 감소
'''

n = int(input())

# 테스트
# n = 36 # 6
# n = 81 # 9
# n = 226576 # 476

start, end = 0, n

while start <= end:
    mid = (start + end) // 2
    temp = mid ** 2

    if temp == n:
        res = mid
        break
    elif temp < n:
        start = mid + 1
    else:
        end = mid - 1

print(res)
