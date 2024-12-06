# 백준 - 실버3 - Anagram - 25099 - 자료 구조(set), 문자열, 정렬 문제
'''
자료 구조(set), 문자열, 정렬 문제

풀이 과정
    1. 입력 받기
    2. 이미 등장한 아나그램을 저장할 set 생성
    3. 결과를 저장할 리스트
    4. 단어를 정렬된 문자열로 변환
    5. 해당 아나그램이 처음 등장하는 경우에만 결과에 추가
    6. 결과 출력
'''

n = int(input())
n_list = [input() for _ in range(n)]

# 테스트
# n = 5
# n_list = ['listen', 'santa', 'satan', 'silent', 'cat'] # listen  \  santa  \  cat

seen_anagrams = set()
res = []

for word in n_list:
    sorted_word = ''.join(sorted(word))

    # 해당 아나그램이 처음 등장하는 경우에만 결과에 추가
    if sorted_word not in seen_anagrams:
        seen_anagrams.add(sorted_word)
        res.append(word)

for word in res:
    print(word)
