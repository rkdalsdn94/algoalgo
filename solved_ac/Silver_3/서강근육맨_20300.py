# 백준 - 실버3 - 서강근육맨 - 20300 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

입력받은 list를 정렬 한 뒤, 그리디하게 문제를 풀면 된다.

풀이 과정
 - 입력받은 n_list 에서 제일 앞에 0을 추가한 다음
 - n_list 의 길이가 2로 나눠진다면 temp에 n_list의 제일 큰 값인 마지막 값을 담아 놓고,
 - 문제에서 한 번 피티를 받을 때마다 두 개의 운동기구를 사용할 수 있다고 한다. 그럼 제일 작은 값과 그 안에서 제일 큰 값을 더해주면 된다.
 - n_list 에서 0번째 인덱스의 값은 임시로 담아놓은 값이므로 무시하고 1 번째 인덱스부터 시작해서 (n // 2 + 1) 의 범위만큼 반복하면서 i와 -i 의 합을 res 에 담는다.
 - res 에 temp 를 추가한 뒤, res 에서 max 값을 출력하면 되는 문제이다.
'''

n = int(input())
n_list = [0] + sorted(list(map(int, input().split())))

# 테스트
# n = 5
# n_list = [0] + sorted([1,2,3,4,5]) # 5

temp = 0
res = []

if n % 2 == 0:
    temp = n_list.pop(-1)

for i in range(1, n // 2 + 1):
    res.append(n_list[i] + n_list[-i])

res.append(temp)
print(max(res))
