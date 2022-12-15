# 백준 - 코스튬 파티 - 실버5 - 완전 탐색, 정렬, 투 포인터 문제
'''
완전 탐색, 정렬, 투 포인터 문제

완전 탐색으로 푸는거면 PyPy3로 제출해야 된다.
투 포인터를 사용하면 Python3으로 제출해도 통과할 수 있다. -> 해당 코드는 제일 아래에 있다.
처음부터 투 포인터로 풀고 싶었는데, 구현이 잘 안떠올랐다.. 그래서, 완전 탐색으로 문제를 풀고 다른 사람의 코드를 참고 했다.
https://bdbest.tistory.com/187 여기서 확인해보면 더 자세한 풀이를 알 수 있다.

풀이 과정
1. input을 다 입력 받은 후 n_list를 오름차순으로 정렬한다.
2. n의 크기만큼 2중 반복문을 실행한 후 각각의 반복문의 인덱스를 더하면서 수의 합이 s보다 작으면 res를 1씩 증가시킨다.
3. res를 출력한다.
'''

n, s = map(int, input().split())
n_list = sorted([ int(input()) for _ in range(n) ])

# 테스트
# n, s = 4, 6
# n_list = sorted([3, 5, 2, 1]) # 4

res = 0

for i in range(n):
    for j in range(i + 1, n):
        if n_list[i] + n_list[j] <= s:
            res += 1

print(res)

'''
n, s = map(int, input().split())
n_list = sorted([ int(input()) for _ in range(n) ])

# 테스트
# n, s = 4, 6
# n_list = sorted([3, 5, 2, 1]) # 4

start, end = 0, n - 1
res = 0

while start <= end:
    if n_list[start] + n_list[end] <= s:
        res += end - start
    else:
        end -= 1
        start -= 1
    start += 1

print(res)
'''