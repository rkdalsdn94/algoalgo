# 백준 - 실버3 - 한국이 그리울 땐 서버에 접속하지 - 9996 - 문자열, 정규 표현식 문제
'''
문자열, 정규 표현식 문제

정규 표현식은 잘 몰라서 필요한 순간에만 검색하고 사용하는데, 이번 문제의 분류가 정규 표현식으로 되어 있어서 풀 수 있을까 걱정을 했는데,
결론적으로 푼 방식은 '*'를 기준으로 split 한 후 앞 부분과, 뒷 부분이 일치하면 'DA' 일치하지 않으면 'NE'를 출력하는 방식으로 풀었다.
일치하는 과정을 검사하는 기준으로 len을 체크하지 않았다가 틀렸었다. (65% 에서 틀렸다면 len 체크를 해야 된다.)

split 한 앞 글자(a)의 길이 + 뒤 글자(b) 글이의 합이 word_list의 원소 값보다 작거나 같아야 된다.
    - 조건식으로 표현하면 다음과 같다. len(i) >= a + b

len 체크 후 word_list의 앞 글자의 값이 일치하는지, 뒤 글자의 값이 일치하는지 이 부분을 검사하면 된다.
문자의 값이 일치하는지 검사는 list splicing 을 사용했다.
    i[:a] -> 앞 글자 일치 여부
    i[-b:] -> 뒤 글자 일치 여부
'''

n = int(input())
target = input().split('*')
word_list = [input() for _ in range(n)]

# 테스트
# n = 3
# target = 'a*d'.split('*')
# word_list = ['abcd', 'anestonestod', 'facebook']  # DA  \  DA  \  NE
# n = 6
# target = 'h*n'.split('*')
# word_list = [
#     'huhovdjestvarnomozedocisvastan', 'honijezakon', 'atila', 'je', 'bio', 'hun'
# ]  # DA  \  DA  \  NE  \  NE  \  NE  \  DA
######### 65% 에서 틀린다면 다음을 검사해보자. #########
# n = 1
# target = 'a*a'.split('*')
# word_list = ['aa'] # DA
# n = 1
# target = 'aaa*a'.split('*')
# word_list = ['aaa'] # NE
# n = 1
# target = 'a*a'.split('*')
# word_list = ['a'] # NE
# n = 1
# target = 'a*ab'.split('*')
# word_list = ['abb']  # NE
# n = 3
# target = 'a*a'.split('*')
# word_list = ['a', 'aa', 'aaa']  # NE  \  DA  \  DA
# n = 1
# target = 'abcd*cdef'.split('*')
# word_list = ['abcdef']
# n = 1
# target = 'abab*abab'.split('*')
# word_list = ['ababab']

for i in word_list:
    a, b = len(target[0]), len(target[1])

    # print(i[:a], i[-b:])
    if i[:a] == target[0] and i[-b:] == target[1] and len(i) >= a + b:
        print('DA')
    else:
        print('NE')
