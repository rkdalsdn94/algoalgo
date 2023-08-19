# 백준 - 브론즈2 - 가장 많은 글자 - 1371 - 구현, 문자열 문제
'''
구현, 문자열 문제

문자열이 얼마나 들어올지 모르니까 무한 루프로 word에 문자열을 계속 입력받고, try except 문법으로 입력이 없을 때(에러 발생) break를 해준다.
입력받은 문자열을 반복하면서 띄어쓰기가 나올 수 있으므로 islower() 함수를 통해 검사한 뒤 소문자가 맞을 때 다음 단계를 실행한다.

word 글자들의 몇 번 나오는지 횟수를 체크 하기 위해 0으로 초기화 한 word_count_list 를 a ~ z 까지의 길이인 26으로 만들어준다.
if 문으로 소문자인 경우들만 분기처리를 하니까 해당 글자를 ord 함수를 통해 유니코드 정수값으로 바꾸고 97을 뺀 뒤 해당 인덱스의 값을 1씩 더해준다.

word_count_list 리스트 변수를 통해 제일 많은 글자와 값이 같으면 해당 글자들을 res에 담고 마지막 res를 출력하면 된다.
'''

word = ''

while 1:
    try:
        word += input()
    except:
        break

# 테스트
# word = '''
# english is a west germanic
# language originating in england
# and is the first language for
# most people in the united
# kingdom the united states
# canada australia new zealand
# ireland and the anglophone
# caribbean it is used
# extensively as a second
# language and as an official
# language throughout the world
# especially in common wealth
# countries and in many
# international organizations
# ''' # a
# word = 'baekjoon online judge' # eno
# word = 'abc a' # a
# word = '''
# abc
# ab
# ''' # ab
# word = '''
# amanda forsaken bloomer meditated gauging knolls
# betas neurons integrative expender commonalities
# latins antidotes crutched bandwidths begetting
# prompting dog association athenians christian ires
# pompousness percolating figured bagatelles bursted
# ninth boyfriends longingly muddlers prudence puns
# groove deliberators charter collectively yorks
# daringly antithesis inaptness aerosol carolinas
# payoffs chumps chirps gentler inexpressive morales
# ''' # e

word_count_list = [0] * 26
res = []

for i in word:
    if i.islower():
        word_count_list[ord(i) - 97] += 1

max_word = max(word_count_list)
for i in range(26):
    if word_count_list[i] == max_word:
        res.append(chr(97 + i))

print(''.join(res))
