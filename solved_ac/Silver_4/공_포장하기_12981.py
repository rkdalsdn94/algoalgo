# 백준 - 실버4 - 공 포장하기 - 12981 - 수학, 그리디, 많은 조건 분기 문제
"""
수학, 그리디, 많은 조건 분기 문제

다른 사람 풀이를 참고해보면 27가지 모든 조건을 직접 나열해서 풀지 않아도 가능하다.
해당 풀이는 `windy7271` 님의 풀이를 참고해보자.

[핵심 아이디어]
    1. 먼저 각 색에서 같은 색 3개씩 묶을 수 있는 최대 박스 개수를 구한다
    2. 나머지 공들(각 색마다 0, 1, 2개)에 대해 가능한 모든 경우를 분석한다
    3. 나머지 공의 조합에 따라 최적의 박스 개수를 직접 계산한다
    4. 총 3^3 = 27가지 경우를 모두 나열하여 처리한다

[풀이 과정]
    1. 각 색의 공을 3으로 나눈 몫을 구하여 같은 색 3개씩 넣는 박스 개수를 계산
    2. 각 색의 공을 3으로 나눈 나머지를 구하여 남은 공의 개수를 파악
    3. 나머지 공들의 조합을 분석:
       - (0,0,0): 추가 박스 불필요
       - (1,1,1): RGB 조합으로 1개 박스
       - (2,2,2): 각 색마다 2개씩이므로 2개 박스
       - (0,1,2), (0,2,1) 등: 서로 다른 색 조합과 같은 색 조합을 적절히 배치
    4. 각 경우에 대해 최소 박스 개수를 직접 계산하여 출력
"""

R, G, B = map(int, input().split())

# 테스트
# R, G, B = 4, 2, 4  # 4
# R, G, B = 1, 7, 1  # 3
# R, G, B = 2, 3, 5  # 4
# R, G, B = 78, 53, 64  # 66
# R, G, B = 100, 100, 100  # 100

# 먼저 각 색에서 같은 색 3개씩 묶을 수 있는 박스 개수 계산
res = 0
res += R // 3 + G // 3 + B // 3
R, G, B = R % 3, G % 3, B % 3

# 나머지 공들의 모든 경우에 대해 최적 박스 개수 계산
if R == 0 and G == 0 and B == 0:
    print(res)  # 나머지 없음
elif R == 1 and G == 1 and B == 1:
    print(res + 1)  # RGB 조합으로 1개 박스
elif R == 2 and G == 2 and B == 2:
    print(res + 2)  # 각 색마다 2개씩, 총 2개 박스
elif R == 0 and G == 1 and B == 2:
    print(res + 2)  # G 1개, BB 1개
elif R == 0 and G == 2 and B == 1:
    print(res + 2)  # GG 1개, B 1개
elif R == 1 and G == 0 and B == 2:
    print(res + 2)  # R 1개, BB 1개
elif R == 1 and G == 2 and B == 0:
    print(res + 2)  # RG 1개, G 1개
elif R == 2 and G == 0 and B == 1:
    print(res + 2)  # RR 1개, B 1개
elif R == 2 and G == 1 and B == 0:
    print(res + 2)  # RR 1개, G 1개
elif R == 0 and G == 0 and B == 1:
    print(res + 1)  # B 1개
elif R == 0 and G == 1 and B == 0:
    print(res + 1)  # G 1개
elif R == 1 and G == 0 and B == 0:
    print(res + 1)  # R 1개
elif R == 0 and G == 2 and B == 0:
    print(res + 1)  # GG 1개
elif R == 2 and G == 0 and B == 0:
    print(res + 1)  # RR 1개
elif R == 1 and G == 1 and B == 0:
    print(res + 1)  # RG 1개
elif R == 1 and G == 0 and B == 1:
    print(res + 1)  # RB 1개
elif R == 0 and G == 1 and B == 1:
    print(res + 1)  # GB 1개
elif R == 2 and G == 1 and B == 1:
    print(res + 2)  # RGB 1개, R 1개
elif R == 1 and G == 2 and B == 1:
    print(res + 2)  # RGB 1개, G 1개
elif R == 1 and G == 1 and B == 2:
    print(res + 2)  # RGB 1개, B 1개
elif R == 2 and G == 2 and B == 1:
    print(res + 2)  # RG 1개, RB 1개
elif R == 2 and G == 1 and B == 2:
    print(res + 2)  # RB 1개, GB 1개
elif R == 1 and G == 2 and B == 2:
    print(res + 2)  # RG 1개, BB 1개
elif R == 0 and G == 0 and B == 2:
    print(res + 1)  # BB 1개
elif R == 0 and G == 2 and B == 2:
    print(res + 2)  # GG 1개, BB 1개
elif R == 2 and G == 0 and B == 2:
    print(res + 2)  # RR 1개, BB 1개
elif R == 2 and G == 2 and B == 0:
    print(res + 2)  # RR 1개, GG 1개
else:
    print(res)
