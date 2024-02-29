# 백준 - 실버3 - 파일 정리 - 20291 - 자료 구조(해시), 문자열, 파싱 문제
'''
자료 구조(해시), 문자열, 파싱 문제

해시(파이썬에서는 dict)을 활용하는 단순한 문제이다.

풀이 과정
 - dic에 값이 있다면 해당 키의 값을 1 더하고, 없다면 해당 키의 값을 1로 초기화한다.
 - dic의 key를 정렬 한 뒤 출력하면 된다.
'''

n = int(input())
n_list = [list(input().split('.')) for _ in range(n)]

# 테스트
# n = 8
# n_list = [
#     list('sbrus.txt'.split('.')),
#     list('spc.spc'.split('.')),
#     list('acm.icpc'.split('.')),
#     list('korea.icpc'.split('.')),
#     list('sample.txt'.split('.')),
#     list('hello.world'.split('.')),
#     list('sogang.spc'.split('.')),
#     list('example.txt'.split('.'))
# ]

dic = {}
for i, j in n_list:
    if j in dic.keys():
        dic[j] += 1
    else:
        dic[j] = 1

for i in sorted(dic.keys()):
    print(i, dic[i])
