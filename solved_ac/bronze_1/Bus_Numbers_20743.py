# 백준 - 브론즈1 - Bus Numbers - 20743 - 수학, 완전 탐색, 런타임 전의 전처리 알고리즘
'''
수학, 완전 탐색, 런타임 전의 전처리 알고리즘

[핵심 아이디어]
    1. 버스 숫자(bus number)는 두 개의 양의 세제곱수의 합으로 최소 2가지 이상 표현 가능한 수입니다.
    2. 입력값 m보다 작거나 같은 수 중에서 가장 큰 버스 숫자를 찾아야 합니다.
    3. 효율적인 계산을 위해 m의 세제곱근까지만 반복문을 실행합니다.
    4. 딕셔너리를 사용하여 각 합과 그것을 만드는 숫자 쌍들을 저장합니다.

[풀이 과정]
    1. 입력값 m의 세제곱근을 계산하여 최대 범위를 설정합니다.
    2. 이중 반복문을 사용하여 가능한 모든 세제곱수의 합을 계산합니다:
       - 바깥 반복문: 1부터 max_cube까지
       - 안쪽 반복문: i부터 max_cube까지 (중복 방지)
    3. 각 합을 키로 하고, 그 합을 만드는 숫자 쌍들을 값으로 하는 딕셔너리를 생성합니다.
    4. 딕셔너리에서 값의 길이가 2 이상인 키들을 찾아 버스 숫자 목록을 만듭니다.
    5. 버스 숫자가 없으면 "none"을, 있다면 그 중 최댓값을 반환합니다.
'''

def find_largest_bus_number(m):
    # 세제곱수의 합으로 표현되는 모든 경우를 저장할 딕셔너리
    cube_sums = {}

    # 세제곱근 계산 (m의 세제곱근보다 작은 수까지만 확인하면 됨)
    max_cube = int(pow(m, 1/3)) + 1

    # 가능한 모든 세제곱수의 합을 계산
    for i in range(1, max_cube + 1):
        for j in range(i, max_cube + 1):  # i부터 시작하여 중복 방지
            sum_of_cubes = i**3 + j**3
            if sum_of_cubes > m:
                break

            # 딕셔너리에 합과 그를 만드는 숫자쌍을 저장
            if sum_of_cubes not in cube_sums:
                cube_sums[sum_of_cubes] = set()
            cube_sums[sum_of_cubes].add((i, j))

    # 2가지 이상의 방법으로 표현되는 수들 중 가장 큰 수 찾기
    bus_numbers = [num for num, pairs in cube_sums.items() if len(pairs) >= 2]

    if not bus_numbers:
        return "none"
    return max(bus_numbers)

m = int(input())

# 테스트
# m = 1730 # 1729
# m = 100 # none

print(find_largest_bus_number(m))
