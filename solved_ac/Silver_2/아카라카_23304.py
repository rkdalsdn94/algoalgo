# 백준 - 실버2 - 아카라카 - 23304 - 문자열, 재귀 문제
'''
문자열, 재귀 문제

처음에 팰린드롬 체크, 접두사와 접미사가 팰린드롬인지 체크만 했는데, 28%에서 틀렸다.
질문 게시판을 참고해보니 문제가 낚시라고한다.
팰린드롬 체크하는 부분을 접두사와 접미사가 팰린드롬인지 체크하는걸 한 번이 아니라 길이가 1이 될 때까지 계속 체크해야 된다.

재귀를 돌면서 인자로 주어진 word의 길이가 1이 되면 끝가지 팰린드롬이 가능한 경우라서 'AKARAKA'를 출력하면 된다.
재귀를 반복하는 중에 입력으로 들어온 글자가 팰린드롬이 완성되지 않으면 'IPSELENTI' 를 출력하면 된다.
'''

s = input()

# 테스트
# s = 'akaraka'  # AKARAKA
# s = 'akbrbka' # IPSELENTI

def recursive(word):
    if len(word) == 1:
        print('AKARAKA')
        return
    if word == word[::-1]:
        recursive(word[:len(word) // 2])
    else:
        print('IPSELENTI')
        return

recursive(s)
