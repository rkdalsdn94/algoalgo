# 프로그래머스 - Lv1 - 키패드 누르기 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

[핵심 아이디어]

[풀이 과정]

'''

def solution(numbers, hand):
    answer = ''
    left, right = [1, 4, 7], [3, 6, 9]
    key_position = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2],
    }
    hand_position = ['*', '#'] # [왼손, 오른손]

    for i in numbers:
        if i in left:
            answer += 'L'
            hand_position[0] = i
        elif i in right:
            answer += 'R'
            hand_position[1] = i
        else:
            # 더 가까운 거리 계산
            near_hand = near_hand_ck(
                key_position, hand_position[0], hand_position[1],
                i, hand
            )

            if near_hand == 'L':
                answer += 'L'
                hand_position[0] = i
            else:
                answer += 'R'
                hand_position[1] = i

    return answer

def near_hand_ck(pos, l, r, target, hand):
    left_distance = abs(pos[l][0] - pos[target][0]) + abs(pos[l][1] - pos[target][1])
    right_distance = abs(pos[r][0] - pos[target][0]) + abs(pos[r][1] - pos[target][1])

    if left_distance == right_distance:
        near_hand = 'L' if hand == 'left' else 'R'
    else:
        near_hand = 'L' if left_distance < right_distance else 'R'

    return near_hand

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")
