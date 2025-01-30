# 백준 - 실버5 - Important Messages - 29934 - 자료 구조(해시) 문제
'''
자료 구조(해시) 문제

[핵심 아이디어]
    1. 해시 테이블(딕셔너리)을 활용하여 연락처 목록을 효율적으로 저장하고 검색
    2. 각 이메일 주소를 키로 하고, 등장 횟수를 값으로 하는 딕셔너리 구조 활용
    3. O(1) 시간 복잡도로 이메일 주소 검색 가능

[풀이 과정]
    1. 연락처 수 N을 입력받고, N개의 이메일 주소를 딕셔너리의 키로 저장 (초기값 0)
    2. 메시지 수 M을 입력받고, M개의 발신자 이메일 주소를 리스트로 저장
    3. 각 메시지의 발신자 주소가 연락처 딕셔너리에 있는지 확인
    4. 있다면 해당 키의 값을 1 증가
    5. 딕셔너리의 모든 값의 합을 출력하여 강조 표시할 메시지 수 계산
'''

n = int(input())
n_dic = {input(): 0 for _ in range(n)}
m = int(input())
m_list = [input() for _ in range(m)]

# 테스트
# n = 3
# n_dic = {
#     'kati@eesti.ee': 0,
#     'lauri@arvuti.net': 0,
#     'mati@eesti.ee': 0
# }
# m = 4
# m_list = [
#     'unknown@somewhere.com',
#     'robot@spam.com',
#     'kati@eesti.ee',
#     'mati@xxx.org'
# ] # 1

for i in m_list:
    if i in n_dic:
        n_dic[i] += 1

print(sum(n_dic.values()))
