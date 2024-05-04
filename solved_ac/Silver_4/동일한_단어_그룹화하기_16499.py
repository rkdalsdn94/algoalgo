# 백준 - 실버4 - 동일한 단어 그룹화하기 - 16499 - 문자열, 자료 구조(해시), 정렬 문제
'''
문자열, 자료 구조(해시), 정렬 문제

처음 제출했을 때 문제를 제대로 이해하지 못해 if 조건을 잘못 써서 틀렸다.
 - 그룹이 2이상 되어야지 res를 1 추가해야 된다고 생각했다.
다시 문제를 파악한 뒤 n_list.count(i) >= 2 이 조건을 빼고 통과했다.

풀이 과정
 1. 입력을 받는다. (n : 단어의 개수, n_list : 단어 리스트)
 2. n_list를 정렬하고, set()을 사용해 중복을 제거한다.
 3. 중복을 제거한 n_list를 ck에 넣고, ck에 없으면 res를 1 추가한다.
 4. res를 출력한다.
'''

n = int(input())
n_list = [sorted(input()) for _ in range(n)]

# n = 4
# n_list = [sorted('cat'), sorted('dog'), sorted('god'), sorted('tca')] # 2
# n = 2
# n_list = [sorted('a'), sorted('a')] # 1
# n = 2
# n_list = [sorted('AB'), sorted('ABB')] # 2

res = 0
ck = set()

for i in n_list:
    if ''.join(i) not in ck: # 처음 n_list.count(i) >= 2 이상이라는 조건을 붙였다가 틀렸었다.
        ck.add(''.join(i))
        res += 1

print(res)
