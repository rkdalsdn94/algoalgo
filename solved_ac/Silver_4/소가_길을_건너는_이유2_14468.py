# 백준 - 실버4 - 소가 길을 거너너는 이유 2 - 14468 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
 - 총 52개의 알파벳 쌍이 2개씩 나오고 겹치는 부분을 찾아야 한다.
 - 선택한 알파벳부터, 다음 알파벳이 나올 때까지 탐색한 뒤, 그 안에 있는 내용물 중에서 알파벳이 1개만 있는 것이 있다면, 경로가 겹치는 것이니 그것을 찾는다.
 - 탐색 진행시 위 예시의 경우 A -> A' 탐색할 때 1번, B -> B' 탐색할 때 1번 해서 가운데가 총 2번 세어지니 최종 결과에선 2를 나눠주면 된다.
'''

s = input()

# 테스트
# s = 'ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ' # 1

result = 0
for start in range(52): # 시작지점부터
    for end in range(start + 1, 52):
        if s[start] == s[end]:
            cows = s[start:end + 1]

            for i in cows:
                if cows.count(i) == 1:
                    result += 1
            break

print(result // 2)

