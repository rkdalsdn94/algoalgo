# 백준 - 두 용액 - 골드5 - 정렬, 투 포인터, 이진 탐색
'''
정렬, 투 포인터, 이진 탐색 문제

처음에 문제가 계속 틀려서 어디가 잘못됐는지 헤매다 눈치 챈 부분이 
pivot 값 설정을 잘 해야 된다. 최소 -1,000,000,000 부터 최대 1,000,000,000 범위라서
1,000,000,001으로 시작했는데 두 값이 더해지는 경우도 있어서 2000000001로 하니까 바로 통과했다.

문제는 투 포인터 방식으로 풀었다. 왼쪽과 오른쪽의 인덱스 값을 미리 설정 후
두 원소를 더한 후 값이 기본 값으로 설정한 값보다 작으면 교체한다.
두 원소를 더한 값이 0보다 작으면 왼쪽을 1 더하고, 작으면 오른쪽을 1 빼면서
처음 왼쪽 값이 오른쪽 값보다 커지는 순간 반복문을 종료하면 된다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 5
# n_list = sorted([-2, 4, -99, -1, 98]) # -99  98

left, right = 0, n - 1
pivot = 2000000001
res = []

while left < right:
    temp = n_list[left] + n_list[right]
    
    if abs(temp) < pivot:
        pivot = abs(temp)
        res = [ n_list[left], n_list[right] ]
    
    if temp < 0:
        left += 1
    else:
        right -= 1

print(*res)