# 백준 - 실버3 - 빈도 정렬 - 2910 - 자료 구조(해시), 정렬 문제
'''
자료 구조(해시), 정렬 문제

python에서 해시를 이용하고 싶으면 딕셔너리를 이용하면 된다.

풀이 과정
temp를 딕셔너리로 선언한 뒤, 입력으로 들어온 n_list의 값들을 키로 1씩 증가시켜 준다. (없으면 1로 만들어줘야 됨)
temp를 정려할 하는데, value 값을 기준으로 정렬할 수 있게 items()와 x[1] 를 적절히 사용하면 된다.
    이 부분이 이해가 안 되면 'python lambda 정렬' 을 찾아보면 된다.

마지막으로 temp 의 값을 반복하면서 i를 list로 만들고, j를 곱한 뒤 res에 더해준다.
res를 출력하면 된다.

문제의 조건 중에 '만약, 등장하는 횟수가 같다면, 먼저 나온 것이 앞에 있어야 한다.' 이 부분을 어떻게 처리할 지 고민하다가,
파이썬의 기본 정렬 함수인 sorted(), sort() 함수는 '안정적인 정렬(Stable Sort)'을 지원한고 알고 있어 따로 처리를 안해도 풀 수 있다.
    (대부분의 언어들은 안정적인 정렬을 지원함)
'''

n, c = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, c = 5, 2
# n_list = [2, 1, 2, 1, 2] # 2 2 2 1 1
# n, c = 9, 3
# n_list = [1, 3, 3, 3, 2, 2, 2, 1, 1] # 1 1 1 3 3 3 2 2 2
# n, c = 9, 77
# n_list = [11, 33, 11, 77, 54, 11, 25, 25, 33]

temp = dict()
res = []

for i in range(n):
    if n_list[i] in temp:
        temp[n_list[i]] += 1
    else:
        temp[n_list[i]] = 1

temp = sorted(temp.items(), key=lambda x:x[1], reverse=True)
for i, j in temp:
    res += [i] * j

print(*res)
