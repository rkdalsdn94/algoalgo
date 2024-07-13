# 백준 - 실버1 - 겹치는 건 싫어 - 20922 - 투 포인터 문제
'''
투 포인터 문제

풀이 과정
1. left, right 포인터를 이용하여 풀이
2. right 포인터를 이동하면서 nums_list에 해당 숫자의 개수를 저장
3. 만약 nums_list[arr[right]]가 k보다 작으면 right를 이동하고, 그렇지 않으면 left를 이동
4. left를 이동할 때는 nums_list[arr[left]]를 1 감소시킴
5. right - left의 최대값을 구하고, 이를 res에 저장
6. res를 출력
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 테스트
# n, k = 9, 2
# arr = [3, 2, 5, 5, 6, 4, 4, 5, 7] # 7
# n, k = 10, 1
# arr = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9] # 6

nums_list = [0] * (max(arr) + 1)
left, right = 0, 0
res= 0

while right < n:
    if nums_list[arr[right]] < k:
        nums_list[arr[right]] += 1
        right += 1
    else:
        nums_list[arr[left]] -= 1
        left += 1

    res = max(res, right - left)

print(res)
