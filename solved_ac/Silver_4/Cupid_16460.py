# 백준 - 실버4 - Cupid - 16460 - 구현, 문자열, 정렬 문제
"""
구현, 문자열, 정렬 문제

[핵심 아이디어]
    프리미엄 사용자의 성별 선호도(F, M, FM, MF)와 최대 지리적 거리 조건을 만족하는 사용자들을 필터링한 후 사전순으로 정렬하여 출력하는 문제이다.

[풀이 과정]
    1. 프리미엄 사용자의 정보(이름, 성별 선호도, 최대 거리) 입력받는다.
    2. N명의 사용자 정보를 순회하며 다음의 조건 확인한다.
       - 성별이 선호도에 맞는지 확인
       - 거리가 제한 범위 내인지 확인
    3. 조건을 만족하는 사용자들을 리스트에 저장한다.
    4. 사전순으로 정렬하여 출력한다.
"""

# 프리미엄 사용자 정보 입력
premium_info = input().split()
n = int(input())
n_list = [input().split() for _ in range(n)]

# 테스트
# premium_info = ["Jason", "F", "20"]
# n = 5
# n_list = [
#     ['Alice', 'F', '37'], ['Bob', 'M', '24'], ['Cristina', 'F', '17'],
#     ['Daniel', 'M', '1'], ['Elle', 'F', '4']
# ] # Cristina  \  Elle
# premium_info = ['RocketMan', 'FM', '200']
# n = 2
# n_list = [['Moon', 'M', '195'], ['Trump', 'M', '11035']] # Moon
# premium_info = ['NoLongDist', 'FM', '1']
# n = 2
# n_list = [['Kim', 'F', '30'], ['Lee', 'M', '19']] # No one yet

premium_name = premium_info[0]
gender_preference = premium_info[1]
max_distance = int(premium_info[2])

# 조건을 만족하는 사용자들을 저장할 리스트
matches = []

# 각 사용자에 대해 조건 확인
for user_info in n_list:
    user_name = user_info[0]
    user_gender = user_info[1]
    distance = int(user_info[2])

    # 거리 조건 확인
    if distance <= max_distance:
        # 성별 선호도 확인
        if gender_preference in ['FM', 'MF']:  # 양성 선호
            matches.append(user_name)
        elif gender_preference == user_gender:  # 특정 성별 선호
            matches.append(user_name)

if matches:
    for match in sorted(matches):
        print(match)
else:
    print("No one yet")
