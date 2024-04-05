# 백준 - 브론즈1 - 문자열 탑 쌓기 - 25643 - 문자열, 완전 탐색 문제
'''
문자열, 완전 탐색 문제

완전 탐색으로 풀면 되는 문제이다.

풀이 과정
1. 입력을 받고, n_list에 저장한다.
2. n_list의 길이만큼 반복문을 돌면서 a, b에 값을 저장한다.
3. flag를 False로 초기화 한 후, a의 뒷 부분과 b의 앞 부분이 같다면 flag를 True로 바꾼다.
4. a의 앞 부분과 b의 뒷 부분이 같다면 flag를 True로 바꾼다.
5. flag가 False라면 0을 출력하고 종료한다.
6. flag가 True라면 1을 출력하고 종료한다.
'''

n, m = map(int, input().split())
n_list = [input() for _ in range(n)]

# 테스트
# n, m = 4, 3
# n_list = ['abc', 'cab', 'bac', 'acb'] # 1
# n, m = 3, 3
# n_list = ['ice', 'oec', 'gym'] # 0

res = True

for i in range(n - 1):
    a, b = n_list[i], n_list[i + 1]
    flag = False

    for j in range(1, m + 1):
        if a[m - j:]  == b[:j]:
            flag = True
            break

        if a[:j] == b[m - j:]:
            flag = True
            break

    if flag == False:
        print(0)
        exit(0)

print(1)
