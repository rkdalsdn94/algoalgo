# 백준 - 실버3 - 눈 치우기 - 26215 - 구현, 그리디, 정렬, 시뮬레이션 문제
'''
구현, 그리디, 정렬, 시뮬레이션 문제

풀이 과정
1. 입력 값을 입력 받는다.
2. 입력 받은 값을 내림차순으로 정렬한다.
3. 가장 큰 값이 1440보다 크면 -1을 출력하고 종료한다.
4. 가장 큰 값이 0이 될 때까지 다음을 반복한다.
    4.1. 리스트의 길이가 1보다 크면
        4.1.1. 가장 큰 값이 0보다 크면 1을 뺀다.
        4.1.2. 두 번째로 큰 값이 0보다 크면 1을 뺀다.
    4.2. 리스트의 길이가 1이면
        4.2.1. 가장 큰 값이 0보다 크면 1을 뺀다.
5. 반복이 끝나면 결과를 출력한다.
'''

n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

# 테스트
# n = 3
# arr = sorted([1, 2, 3], reverse=True) # 3
# n = 3
# arr = sorted([1, 2, 5], reverse=True) # 5
# n = 1
# arr = sorted([1441], reverse=True) # -1
# n = 1
# arr = sorted([1440], reverse=True) # 1440

res = 0

if arr[0] > 1440:
    print(-1)
    exit(0)

while arr[0] > 0:
    if len(arr) > 1:
        if arr[0] > 0:
            arr[0] -= 1
        if arr[1] > 0:
            arr[1] -= 1
    else:
        arr[0] -= 1

    res += 1
    arr.sort(reverse=True)

print(res)
