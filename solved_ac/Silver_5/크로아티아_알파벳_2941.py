'''
문자열을 입력받고, 문제 중에 있는 크로아티아 알파벳을 정의 한 후
문자열에서 replace로 반환하기 (최대 100글자라 막 구현해도 괜찮음)
최종 출력에선 일반 알파벳 + 크로아티아 알파벳의 길이로 출력해야된다.
'''

word = input()

# 테스트
# word = 'ljes=njak' # 6
# word = 'ddz=z=' # 3
# word = 'nljj' # 3
# word = 'c=c=' # 2
# word = 'dz=ak' # 3

croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_alphabet:
    word = word.replace(i, '@')

print(len(word))
