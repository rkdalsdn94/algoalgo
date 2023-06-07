# 백준 - 실버5 - 카약과 강풍 - 2891 - 구현, 그리디 문제
'''
구현, 그리디 문제

N : 첫째 줄에 팀의 수
S : 카약이 손상된 팀의 수
R : 카약을 하나 더 가져온 팀의 수

계속 76% 에서 틀렸다가 질문 게시판에 있는 https://www.acmicpc.net/board/view/118167 이 질문의 답글을 보고 해결할 수 있었다.
답글에 핵심은 다음과 같다. 'S와 R을 직접 수정하지 말고, 다른 배열을 추가로 사용하시는걸 추천드립니다.'
위 내용 통해 temp 리스트를 만들고 제거해야 될 대상을 append 한 후, 마지막 for 문을 시작하전에 제거하면 된다.
'''

n, s, r = map(int, input().split())
s_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

# 테스트
# n, s, r = 5, 2, 1
# s_list = [2, 4]
# r_list = [3] # 1
####################################################
# n, s, r = 5, 2, 3
# s_list = [2, 4]
# r_list = [1, 3, 5] # 0
####################################################
# n, s, r = 10, 1, 1
# s_list = [1]
# r_list = [3] # 1
####################################################
# n, s, r = 10, 5, 2
# s_list = [1, 2, 3, 6, 7]
# r_list = [7, 8] # 4
####################################################
# n, s, r = 5, 3, 3
# s_list = [2, 3, 4]
# r_list = [1, 2, 3] # 1

res = 0
temp = []

for i in r_list:
    if i in s_list:
        temp.append(i)

for i in temp: # 카약을 하나 더 가져온 팀의 카약이 손상되었다면, 여분의 카약으로 경기에 출전하게되고, 이 카약은 다른 팀에게 빌려줄 수 없다.
    r_list.remove(i)
    s_list.remove(i)

for i in s_list: # 여분의 카약이 다른 팀을 빌려줄 수 있는 경우
    if i - 1 in r_list:
        r_list.remove(i - 1)
    elif i + 1 in r_list:
        r_list.remove(i + 1)
    else: # 여분의 카약이 -1, +1 범위에 없으면 출발할 수 없다.
        res += 1

print(res)
