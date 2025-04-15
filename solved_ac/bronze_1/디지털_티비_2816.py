# 백준 - 실버3 - 리모컨 - 2959 - 구현, 해 구성하기 문제
"""
구현, 해 구성하기 문제

[핵심 아이디어]
    1. KBS1을 첫 번째로, KBS2를 두 번째로 이동시키기 위한 리모컨 조작 시퀀스를 구한다.
    2. 리모컨의 4가지 버튼을 이해하고 적절히 사용한다:
       - 1번: 화살표를 아래로 한 칸 이동
       - 2번: 화살표를 위로 한 칸 이동
       - 3번: 현재 선택한 채널을 아래로 한 칸 이동(스왑)
       - 4번: 현재 선택한 채널을 위로 한 칸 이동(스왑)
    3. KBS1을 먼저 첫 번째 위치로 옮기고, 그 다음 KBS2를 두 번째 위치로 옮긴다.

[풀이 과정]
    1. KBS1 처리:
       - 화살표를 KBS1 위치로 이동 (1번 또는 2번 버튼 사용)
       - KBS1을 첫 번째 위치로 이동 (4번 버튼 반복 사용)
    2. KBS2 처리:
       - KBS1 이동 후 KBS2의 새 위치 계산
       - 화살표를 KBS2 위치로 이동 (1번 또는 2번 버튼 사용)
       - KBS2를 두 번째 위치로 이동 (4번 버튼 반복 사용)
"""

n = int(input())
channels = [input() for _ in range(n)]

# 테스트
# n = 3
# channels = ['MBC', 'KBS1', 'KBS2'] # 33 or 14114
# n = 4
# channels = ['ABC1', 'ABC02', 'KBS2', 'KBS1'] # 11144411144
# n = 4
# channels = ['ABC1', 'ABC02', 'KBS2', 'KBS1'] # 33144413 or 11144411144

# KBS1과 KBS2의 위치 찾기
kbs1_idx = channels.index("KBS1")
kbs2_idx = channels.index("KBS2")

result = ""

# 채널의 현재 상태를 시뮬레이션
current_channels = channels.copy()
cursor = 0  # 화살표 위치

# 1. KBS1을 첫 번째 위치로 이동
# 1-1. 화살표를 KBS1 위치로 이동
while cursor < kbs1_idx:
    result += "1"
    cursor += 1

# 1-2. KBS1을 첫 번째 위치로 이동
while cursor > 0:
    # 채널 위치 변경 (현재 선택한 채널을 위로 이동)
    current_channels[cursor], current_channels[cursor-1] = current_channels[cursor-1], current_channels[cursor]
    result += "4"
    cursor -= 1

# 이제 KBS1은 첫 번째 위치에 있고, 화살표는 0번 인덱스를 가리킴

# 2. KBS2를 두 번째 위치로 이동
# KBS1 이동 후 KBS2의 새 위치 계산
if kbs2_idx > kbs1_idx:
    kbs2_new_idx = kbs2_idx - 1
else:
    kbs2_new_idx = kbs2_idx

# 현재 채널 배열에서 KBS2의 위치 찾기
kbs2_current_idx = current_channels.index("KBS2")

# 2-1. 화살표를 KBS2 위치로 이동
while cursor < kbs2_current_idx:
    result += "1"
    cursor += 1

# 2-2. KBS2를 두 번째 위치로 이동
while cursor > 1:  # KBS2가 두 번째 위치에 있어야 함
    # 채널 위치 변경 (현재 선택한 채널을 위로 이동)
    current_channels[cursor], current_channels[cursor-1] = current_channels[cursor-1], current_channels[cursor]
    result += "4"
    cursor -= 1

print(result)
