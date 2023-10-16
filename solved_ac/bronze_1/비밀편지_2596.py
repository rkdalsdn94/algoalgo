# 백준 - 브론즈1 - 비밀편지 - 2596 - 구현, 문자열 문제
'''
구현, 문자열 문제

딕셔너리(character_dict)로 숫자를 키로 문자를 값으로 미리 만들어 놓는다.
입력으로 들어오는 숫자를 6자씩 쪼개 word_list에 담아주고, 해당 word_list의 값들로 반복문을 진행한다.

반복문 내에서 글자가 없을 경우를 대비해 cnt라는 변수를 word_list의 글자가 시작할 때마다 1씩 증가시킨다.
word_list의 숫자로 되어있는 글자가 character_dict에 존재한다면 해당 값을 res에 담아주고,
존재하지 않는다면 딕셔너리 키들로만 반복문을 다시 시작한다. (시작하기 전 글자를 세기 위한 temp변수도 미리 0으로 초기화)
    딕셔너리 키로 반복문을 진행하면서 글자가 다른지 비교하기 위해 word_check_cnt 변수를 사용하고,
    각 글자가 다른지 체크하기 위해 6 글자씩 반복문을 진행하고, 다른 글자가 있을 때마다 word_check_cnt 변수를 1씩 더한다.
    만약, word_check_cnt 변수의 값이 1보다 작거나 같다면 한 글자만 다른 경우이므로 해당 키의 값을 res에 담아주고,
    그게 아니라면 temp의 값을 증가시킨다.

위 반복문으 종료되고 temp의 값이 character_dict의 길이와 같다면
    두 글자 이상씩 모든 글자와 다른 경우라 위에서 정의해 둔 cnt를 출력하고 프로그램을 종료 시킨다.

이때까지 프로그램이 종료되지 않았다면 res를 출력하면 된다.
'''

n = int(input())
word = input()

# 테스트
# n = 3
# word = '001111000000011100' # BAD
# n = 5
# word = '011111000000111111000000111111' # 3

character_dict = {
    '000000': 'A',
    '001111': 'B',
    '010011': 'C',
    '011100': 'D',
    '100110': 'E',
    '101001': 'F',
    '110101': 'G',
    '111010': 'H'
}
word_list = []
res = ''
cnt = 0

for i in range(0, len(word), 6):
    word_list.append(word[i:i + 6])

for i in word_list:
    cnt += 1

    if i in character_dict:
        res += character_dict[i]
    else:
        temp = 0
        for j in character_dict.keys():
            word_check_cnt = 0

            for k in range(6):
                if j[k] != i[k]:
                    word_check_cnt += 1
            if word_check_cnt <= 1:
                res += character_dict[j]
                break
            else:
                temp += 1
        if temp == len(character_dict):
            print(cnt)
            exit(0)

print(res)
