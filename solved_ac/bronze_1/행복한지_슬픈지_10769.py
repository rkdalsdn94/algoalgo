# 백준 - 브론즈1 - 행복한지 슬픈지 - 10769 - 문자열, 파싱 문제
'''
문자열, 파싱 문제

다음의 요구사항을 구현하면 되는 문제이다. (요구사항 중 각각의 이모티콘은 다음과 같다. 행복한 이모티콘 - ':-)', 슬픈 이모티콘 - ':-(')
- 어떤 이모티콘도 포함되어 있지 않으면, none 을 출력한다.
- 행복한 이모티콘과 슬픈 이모티콘의 수가 동일하게 포함되어 있으면, unsure 를 출력한다.
- 행복한 이모티콘이 슬픈 이모티콘보다 많이 포함되어 있으면, happy 를 출력한다.
- 슬픈 이모티콘이 행복한 이모티콘보다 많이 포함되어 있으면, sad 를 출력한다.

input 으로 들어오는 word의 각각의 이모티콘을 count 해서 상황에 맞게 출력하면 되는 단순한 문제이다.
'''

word = input()

# 테스트
# word = 'How are you :-) doing :-( today :-)?' # happy
# word = ':)' # none
# word = 'This:-(is str:-(:-(ange te:-)xt.' # sad

happy_cnt, sad_cnt = word.count(':-)'), word.count(':-(')

if happy_cnt > sad_cnt:
    print('happy')
elif happy_cnt < sad_cnt:
    print('sad')
elif sad_cnt != 0 and happy_cnt == sad_cnt:
    print('unsure')
else:
    print('none')
