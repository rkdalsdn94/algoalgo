# 백준 - 다음 순열 - 실버3 - 10972 - 수학, 조합 문제
'''
수학, 조합 문제

시간 제한만 없다면 permutations 을 이용해서 풀 수도 있는 문제지만 해당 문제는 시간 제한이 존재한다.
그래서, 아래 경우에만 n_list를 수정하면 된다.

 - n_list의 길이 - 1 부터 시작해서 이 전의 값이 현재 값보다 작으면
     새로운 반복문을 통해 새로운 반복문과 처음 시작한 i의 전 값을 비교한 후 스왑한 다음 n_list를 다시 만들고 출력하면 된다.
 - 처음 반복문을 다 돌면서 작은 값이 없다면 -1을 출력한다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 4
# n_list = [1,2,3,4] # 1 2 4 3
# n = 5
# n_list = [5,4,3,2,1] # -1

flag = False

for i in range(n - 1, 0, -1):
    if n_list[i - 1] < n_list[i]:
        for j in range(n - 1, 0, -1):
            if n_list[i - 1] < n_list[j]:
                n_list[i - 1], n_list[j] = n_list[j], n_list[i - 1]
                n_list = n_list[:i] + sorted(n_list[i:])
                flag = True
                break
    if flag:
        print(*n_list)
        break

if not flag:
    print(-1)
