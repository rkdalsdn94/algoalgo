# 백준 - 실버5 - 브실이의 입시전략 - 29723 - 자료 구조(해시), 정렬 문제
'''
자료 구조(해시), 정렬 문제

입력으로 들어온 값을 정렬한 후, 최소값과 최대값을 출력하는 문제이다.
문제를 잘 파악해야 된다. 오픈된 과목과 닫힌 과목을 마지막으로 구해야 한다.
    for i in range(m - k) 범위로 구해야 된다.
    예제만 신경 쓰고 풀었다가 한 번 틀렸다...

풀이 과정
    1. 각각 상황에 맞게 입력을 받는다. (딕셔너리로 받아야 부분도 신경써야 됨)
    2. 오픈된 과목(k_list)들의 점수를 public_subject_score에 더한다.
    3. 오픈된 과목(k_list)들을 딕셔너리에서 삭제한다.
    4. 딕셔너리를 정렬한다.
    5. m - k 범위로 최솟값과 최댓값을 구한다.
'''

n, m, k = map(int, input().split())
n_dic = {}
for _ in range(n):
    a, b = input().split()
    n_dic[a] = int(b)
k_list = [input() for _ in range(k)]

# 테스트
# n, m, k = 6, 3, 2
# n_dic = {
#     'calculus': 100, 'probability': 70, 'physics': 50,
#     'chemistry': 80, 'python': 90, 'algorithm': 100
# }
# k_list = ['physics', 'python'] # 210 240

public_subject_score = 0
for i in k_list:
    public_subject_score += n_dic[i]
    del n_dic[i]

n_dic = sorted(n_dic.items(), key=lambda x: x[1], reverse=True)
min_res, max_res = public_subject_score, public_subject_score

for i in range(m - k):
    min_res += n_dic[-i - 1][1]
    max_res += n_dic[i][1]

print(min_res, max_res)
