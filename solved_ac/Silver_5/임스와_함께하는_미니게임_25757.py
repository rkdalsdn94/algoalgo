# 백준 - 실버5 - 임스와 함께하는 미니게임 - 25757 - 자료 구조(set), 문자열 문제
'''
자료 구조(set), 문자열 문제

set을 사용해 중복을 제거한 후, 각 게임에 따라서 출력하면 되는 간단한 문제이다.
윷놀이(Y), 같은 그림 찾기(F), 원카드(O) 게임들은 각각 2명 3명 4명의 인원이 필요

풀이 과정
1. 입력을 set comprehension을 사용하여 중복을 제거한 인원을 구한다.
2. 문제에 주어진 게임을 진행할 때 필요한 인원을 생각해 구하면 된다.
    2.1. 임스를 제외한 인원이 필요하므로, 윷놀이는 2 - 1, 같은 그림 찾기는 3 - 1, 원카드는 4 - 1이다.
3. 따라서 윷놀이는 set의 len을 그대로 출력하고 같은 그림 찾기와 원카드는 각각 // 2, // 3 한 값으로 출력하면 된다.
'''

n, game = input().split()
n = int(n)
n_set = {input() for _ in range(n)}

# 테스트
# n, game = 7, 'Y'
# n_set = {
#     'lms0806', 'lms0806', 'exponentiale', 'lms0806',
#     'jthis', 'lms0806', 'leo020630'
# } # 4
# n, game = 12, 'F'
# n_set = {
#     'lms0806', 'powergee', 'skeep194', 'lms0806',
#     'tony9402', 'lms0806', 'wider93', 'lms0806',
#     'mageek2guanaah', 'lms0806', 'jthis', 'lms0806',
# } # 3
# n, game = 7, 'O'
# n_set = {
#     'lms0806', 'mageek2guanaah', 'jthis', 'lms0806',
#     'exponentiale', 'lms0806', 'leo020630', 'lms0806',
#     'powergee', 'lms0806', 'skeep194', 'lms0806',
# } # 2

if game == 'Y':
    print(len(n_set))
elif game == 'F':
    print(len(n_set) // 2)
elif game == 'O':
    print(len(n_set) // 3)
