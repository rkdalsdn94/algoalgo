# 백준 - 실버3 - 카드게임 - 2621 - 구현 문제
'''
구현 문제

문제에 주어진 규칙을 구현하면 되는 문제인데, 신경쓸게 많아서 생각보다 복잡한 문제이다.
문제에 있는 <점수를 정하는 규칙>을 각각 테스트 한 뒤에 출력했다.
7, 8은 겹치는 부분이 있어서 if문 안에 로직을 구현한 후 검사하는 방식으로 진행했다.
코드를 천천히 읽어보면 이해할 수 있다.
'''

card_color_list = []
card_number_list = []
card_character_dict = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
new_card_number_list = [ 0 for _ in range(10) ]

for _ in range(5):
    a, b = input().split()
    card_color_list.append(a)
    card_number_list.append(int(b))
# print(card_color_list, card_number_list)

# 테스트
# 예제
# card_color_list = [ 'B', 'B', 'R', 'B', 'Y' ]
# card_number_list = [ 3, 7, 1, 2, 7 ] # 207

# # 1
# card_color_list = [ 'Y', 'Y', 'Y', 'Y', 'Y' ]
# card_number_list = [ 4, 3, 2, 5, 6 ] # 906

# # 2
# card_color_list = [ 'B', 'R', 'B', 'Y', 'G' ]
# card_number_list = [ 3, 3, 7, 3, 3 ] # 803

# # 3
# card_color_list = [ 'R', 'Y', 'G', 'B', 'Y' ]
# card_number_list = [ 5, 5, 7, 5, 7 ] # 757

# # 4
# card_color_list = [ 'Y', 'Y', 'Y', 'Y', 'Y' ]
# card_number_list = [ 3, 4, 8, 6, 7 ] # 608

# # 5
# card_color_list = [ 'R', 'R', 'G', 'Y', 'B' ]
# card_number_list = [ 7, 8, 9, 6, 5 ] # 509

# # 6
# card_color_list = [ 'R', 'Y', 'R', 'G', 'R' ]
# card_number_list = [ 7, 7, 2, 7, 5 ] # 407

# # 7
# card_color_list = [ 'R', 'Y', 'Y', 'G', 'B' ]
# card_number_list = [ 5, 5, 4, 9, 4 ] # 354

# # 8
# card_color_list = [ 'R', 'Y', 'B', 'B', 'G' ]
# card_number_list = [ 5, 2, 5, 3, 4 ] # 205

# # 9
# card_color_list = [ 'R', 'R', 'B', 'B', 'G' ]
# card_number_list = [ 1, 2, 4, 8, 5 ] # 108

res = 0

for i in card_color_list:
    card_character_dict[i] += 1
for i in card_number_list:
    new_card_number_list[i] += 1

def successive_number_check(card_number_list):
    temp = 1

    for i in range(len(card_number_list) - 1):
        if card_number_list[i] + 1 == card_number_list[i + 1]:
            temp += 1
    
    return temp

# 1
if 5 in card_character_dict.values() and successive_number_check(sorted(card_number_list)) == 5:
    res += max(card_number_list) + 900
# 2
elif 4 in new_card_number_list:
    res += new_card_number_list.index(4) + 800
# 3
elif 3 in new_card_number_list and 2 in new_card_number_list:
    res += new_card_number_list.index(3) * 10 + new_card_number_list.index(2) + 700
# 4
elif 5 in card_character_dict.values():
    res += max(card_number_list) + 600
# 5
elif successive_number_check(sorted(card_number_list)) == 5:
    res += max(card_number_list) + 500
# 6
elif 3 in new_card_number_list:
    res += new_card_number_list.index(3) + 400
# 7, 8
elif 2 in new_card_number_list:
    aa = new_card_number_list.index(2)
    bb = card_number_list.copy()

    for i in bb:
        if i == aa:
            card_number_list.remove(i)
    new_card_number_list[aa] = 0
    if 2 in new_card_number_list:
        cc = new_card_number_list.index(2)
        res += max(aa, cc) * 10 + min(aa, cc) + 300 # 7
    else:
        res += aa + 200 # 8
# 9
else:
    res += max(card_number_list) + 100

print(res)
