'''
문자열 그대로 index를 적용하고 싶어서 number_set = [0] * 10 이렇게 했다. (10으로 곱했다.)
그리고 해당 문자를 한글자씩 돌면서 numbser_set의 해당 인덱스 값을 +1 한 후에,
max값으로 반환했다.
'''

n = input()

# 테스트
# n = '9999' # 2
# n = '122' # 2
# n = '12635' # 1
# n = '888888' # 6

number_set = [0] * 10

for i in range(len(n)):
    word = int(n[i])

    if word == 6 or word == 9:
        if number_set[6] <= number_set[9]:
            number_set[6] += 1
        else:
            number_set[9] += 1
    else:
        number_set[word] += 1

print(max(number_set))

