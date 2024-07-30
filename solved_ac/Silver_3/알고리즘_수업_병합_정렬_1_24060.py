# 백준 - 실버3 - 알고리즘 수업 병합 정렬 1 - 24060 - 구현, 정렬, 재귀 문제
'''
구현, 정렬, 재귀 문제

문제에 나와 있는 merge sort를 구현하면 되는 문제이다.

풀이 과정
    1. 입력을 받는다.
    2. merge_sort 함수를 만들어서 정렬을 한다.
        2.1. merge_sort 함수는 start와 end를 받아서 재귀적으로 정렬을 한다.
        2.2. merge 함수는 start, q, end를 받아서 정렬을 한다.
    3. merge 함수에서 cnt가 k와 같아지면 res에 값을 저장하고, 출력한다.
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 테스트
# n, k = 5, 7
# arr = [4, 5, 1, 3, 2] # 3
# n, k = 5, 13
# arr = [4, 5, 1, 3, 2]  # -1

def merge_sort(arr, start, end):
    if start < end:
        q = (start + end) // 2
        merge_sort(arr, start, q)
        merge_sort(arr, q + 1, end)
        merge(arr, start, q, end)

def merge(arr, start, q, end):
    global cnt, res
    i = start
    j = q + 1
    temp = []

    while i <= q and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= q:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j += 1

    i = start
    idx = 0

    while i <= end:
        arr[i] = temp[idx]
        cnt += 1

        if cnt == k:
            res = arr[i]
            break
        i += 1
        idx += 1

cnt = 0
res = -1
merge_sort(arr, 0, n - 1)
print(res)
