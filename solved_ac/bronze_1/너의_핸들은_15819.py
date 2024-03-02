# 백준 - 브론즈1 - 너의 핸들은 - 15819 - 단순 구현, 정렬 문제
'''
단순 구현, 정렬 문제

풀이 과정이라고 할 것이 따로 없다.
입력 받은 값들을 정렬 후 l번째 값을 출력하면 되는 간단한 문제이다.
'''

n, l = map(int, input().split())
n_list = sorted([input() for _ in range(n)])

# 테스트
# n, l = 4, 1
# n_list = sorted(['acka1357', 'spectaclehong', 'mitslll', 'luke0201']) # acka1357
# n, l = 9, 7
# n_list = sorted(['tourist', 'petr', 'qilip', 'won0114', 'hmy3743', 'jujh97', 'hjhj97', 'bio8641', 'kangjieun9843']) # acka1357

print(n_list[l - 1])
