# 백준 - 실버5 - 세 부분 - 2993 - 구현, 문자열, 완전 탐색, 정렬 문제
'''
구현, 문자열, 완전 탐색, 정렬 문제

문제의 핵심 요구사항
  - 단어를 세 부분으로 나눔
  - 각 부분을 뒤집음
  - 다시 합쳐서 사전순으로 가장 앞선 단어를 찾음

풀이 과정
    1. 단어를 입력받음
    2. 단어를 세 부분으로 나누어 뒤집음
    3. 세 부분을 합쳐서 사전순으로 가장 앞선 단어를 찾음
    4. 결과를 출력함
'''

word = input()

# word = 'dcbagfekjih' # abcdefghijk
# word = 'mobitel' # bometil
# word = 'anakonda' # aanadnok

res = []
# 1. 첫 번째 for문: i는 첫 번째 부분의 시작 위치
for i in range(len(word) - 2):  # 0부터 len(word)-3까지
    # 2. 두 번째 for문: j는 두 번째 부분의 시작 위치
    for j in range(i + 1, len(word) - 1):
        # 3. 세 번째 for문: k는 세 번째 부분의 시작 위치
        for k in range(j + 1, len(word)):
            # 4. 원본 단어 길이와 세 부분을 합친 길이가 같은지 확인
            if len(word) == len(word[i:j] + word[j:k] + word[k:]):
                # 5. 세 부분으로 나누기
                a, b, c = word[i:j], word[j:k], word[k:]
                # 6. 각 부분을 뒤집어서 합친 후 결과 리스트에 추가
                res.append([a[::-1] + b[::-1] + c[::-1]])

# 7. 모든 가능한 결과를 정렬
res.sort()
# 8. 사전순으로 가장 앞선 결과 출력
print(''.join(res[0]))
