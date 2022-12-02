# 백준 - 좋은 구간 - 실버4 - 1059 - 수학, 정렬, 완전 탐색 문제
'''
수학, 정렬, 완전 탐색 문제

처음에 제한 사항중 '1 ≤ n ≤ (집합 S에서 가장 큰 정수)' 여기 부분이 정확하게 이해가 되지 않아 고민을 꽤 했다..
ㄴ> 내가 문제를 대충 읽어서 발생한 문제이다... 그 위에 좋은 구간의 조건 중 'A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.' 이게 있다.
ㄴ> '1 ≤ n ≤ (집합 S에서 가장 큰 정수)' 이 말을 다른말로 S에서 n보다 큰 값중 제일 작은 값으로 해석해도 무방하다.

풀이 과정
1. input을 잘 입력 받고, 입력받은 n이 s_list안에 있다면 좋은 구간을 찾을수 없으므로 0을 출력하고 종료한다.
2. s_list 안에서 n보다 작은 값과 n보다 큰 값중 제일 작은 값을 찾기 위해 s_min, s_max라는 변수를 각각 0으로 초기화 한고, 정답 출력을 위해 res변수도 초기화 한다.
3. 입력받은 후 오름차순 정렬을 진행한 s_list의 값을 하나 씩 꺼내서 해당 값이 n보다 작으면 s_min으로 만들어 준다.
4. 하나 씩 꺼낸 i의 값이 n보다 크면 S에서 n보다 큰 값중 제일 작은 값이므로 해당 i를 s_max에 대입하고 반복문을 종료한다.
5. s_min + 1 (s_min은 S에 속하므로..) 부터 s_max 까지 i <= n <= j의 조건의 속하면 res를 1씩 더한다.
6. res를 출력한다.
'''

s_count = int(input())
s_list = sorted(list(map(int, input().split())))
n = int(input())

# 테스트
# s_count = 4
# s_list = sorted([1,7, 14, 10])
# n = 2 # 4
# s_count = 5
# s_list = sorted([4,8,13,24,30])
# n = 10 # 5
# s_count = 5
# s_list = sorted([10,20,30,40,50])
# n = 30 # 0
# s_count = 8
# s_list = sorted([3,7,12,18,25, 100, 33, 1000])
# n = 59 # 1065

if n in s_list:
    print(0)
    exit(0)

s_min, s_max = 0, 0
res = 0

for i in s_list:
    if i < n:
        s_min = i
    elif i > n:
        s_max = i
        break

for i in range(s_min + 1, s_max - 1):
    for j in range(i + 1, s_max):
        if i <= n <= j:
            res += 1

print(res)
