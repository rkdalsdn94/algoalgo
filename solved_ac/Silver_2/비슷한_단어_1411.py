# 백준 - 실버2 - 비슷한 단어 - 1411 - 문자열, 완전 탐색 문제
'''
문자열, 완전 탐색 문제

딕셔너리를 잘 활용하고, 완전 탐색으로 풀면 되는 문제이다.

풀이 과정
입력으로 들어오는 단어의 모든 글자를 완전 탐색하고, 딕셔너리에 방문하는 글자가 없을 경우 temp_num 이라는 값으로 담는다.
    딕셔너리에 temp_num을 담은 후 다른 글자가 들어올 경우를 대비해 temp_num을 1씩 증가시켜야 한다.
temp_num을 temp에 append 시킨다. (최종적으로 글자를 비교하기 위해)
위 과정을 n번 반복하고, 모든 글자를 순회하면 temp에는 n만큼의 temp_num으로 이루어진 리스트들이 들어옸고,
해당 temp[i]랑 다음번째 temp[i + 1:]에서 같은 값이 있는지 비교한 뒤, 같은 값이 있을 때마다 res를 1씩 더하면 된다.
'''

n = int(input())
word_list = [input() for _ in range(n)]

# 테스트
# n = 5
# word_list = ['aa', 'ab', 'bb', 'cc', 'cd'] # 4
# n = 3
# word_list = ['abca', 'zbxz', 'opqr'] # 1
# n = 12
# word_list = [
#     'cacccdaabc',
#     'cdcccaddbc',
#     'dcdddbccad',
#     'bdbbbaddcb',
#     'bdbcadbbdc',
#     'abaadcbbda',
#     'babcdabbac',
#     'cacdbaccad',
#     'dcddabccad',
#     'cacccbaadb',
#     'bbcdcbcbdd',
#     'bcbadcbbca'
# ] # 13

temp = [[] for _ in range(n)]
dic = [dict() for _ in range(n)]
res = 0

for i in range(n):
    temp_num = 0

    for j in word_list[i]:
        if j not in dic[i]:
            dic[i][j] = str(temp_num)
            temp_num += 1
        temp[i].append(dic[i][j])

for i in range(n):
    for j in range(i + 1, n):
        if temp[i] == temp[j]:
            res += 1

print(res)
