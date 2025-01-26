# 백준 - 브론즈1 - 전주 듣고 노래 맞히기 - 31562 - 구현, 자료 구조(해시), 문자열, 완전 탐색 문제
'''
구현, 자료 구조(해시), 문자열, 완전 탐색 문제

[핵심 아이디어]
1. 딕셔너리(해시)를 사용하여 노래의 첫 3개 음을 키로, 노래 제목을 값으로 저장
2. 첫 3개 음이 같은 노래가 여러 개일 수 있으므로, 딕셔너리의 값을 리스트로 관리
3. 입력된 3개 음에 대해 딕셔너리를 검색하여 조건에 따라 결과 출력
   - 매칭되는 노래가 1개: 노래 제목 출력
   - 매칭되는 노래가 2개 이상: "?" 출력
   - 매칭되는 노래가 없음: "!" 출력

[풀이 과정]
1. 입력 처리
   - N개의 노래 정보와 M개의 테스트 케이스를 입력받음
   - 테스트 케이스는 공백을 제거하여 문자열로 저장

2. 노래 정보 저장
   - 각 노래의 정보를 분리하여 첫 3개 음을 키로 사용
   - 딕셔너리에 노래 제목을 리스트 형태로 저장
   - 같은 음으로 시작하는 노래는 리스트에 추가

3. 결과 출력
   - M개의 테스트 케이스에 대해 딕셔너리 검색
   - 검색 결과에 따라 노래 제목, "?", 또는 "!" 출력
'''

n, m = map(int, input().split())
n_list = [input() for _ in range(n)]
m_list = [''.join(input().split()) for _ in range(m)]

# 테스트
# n, m = 4, 4
# n_list = [
#     '11 TwinkleStar C C G G A A G',
#     '8 Marigold E D E F E E D',
#     '23 DoYouWannaBuildASnowMan C C C G C E D',
#     '12 Cprogramming C C C C C C C'
# ]
# m_list = [
#     ''.join('E D E'.split()),
#     ''.join('C G G'.split()),
#     ''.join('C C C'.split()),
#     ''.join('C C G'.split())
# ] # Marigold  \  !  \  ?  \  TwinkleStar

song_dic = {}
for i in n_list:
    t, s, *scale = i.split()
    scale = ''.join(scale)[:3]

    if scale in song_dic:
        song_dic[scale].append(s)
    else:
        song_dic[scale] = [s]

for i in m_list:
    if i in song_dic and len(song_dic[i]) == 1:
        print(*song_dic[i])
    elif i in song_dic and len(song_dic[i]) >= 2:
        print('?')
    else:
        print('!')
