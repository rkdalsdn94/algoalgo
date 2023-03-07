# 백준 - 실버5 - 이름 궁합 - 15312 - 구현, 문자열 문제
'''
구현, 문자열 문제

a와 b의 길이가 같고, a부터 시작하라고 문제에 명시되어 있다.
따라서, a와 b 한 글자씩 이름 궁합을 위해 name_compatibility 라는 리스트에 a부터 시작해서 해당 글자의 획을 append 한다.
(획을 구하는 법은 대문자로 되어 있으니까 65를 빼거나, 나머지르 연산자를 이용해서 해당 인덱스를 구하면 된다.)

name_compatibility 리스트의 길이가 2보다 클 경우 1부터 시작하는 for 반복문을 실행해서 이름 궁합을 맞춰준다.
(10보다 큰 경우에만 10을 나머지 연산자를 이용해 일의 자리만 구한다.)

길이가 2가 된 name_compatibility 리스트를 출력 형식에 맞춰 출력하면 된다.
나는 join과 map을 이용해 문자열로 만든 후 출력했다.
'''

a, b = input(), input()

# 테스트
# a, b = 'CJM', 'HER' # 99

alphabet_num_list = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
name_compatibility = []

for i, j in zip(a, b):
    name_compatibility.append(alphabet_num_list[ord(i) % 65])
    name_compatibility.append(alphabet_num_list[ord(j) % 65])

while len(name_compatibility) > 2:
    temp = []

    for i in range(1, len(name_compatibility)):
        temp_num = name_compatibility[i - 1] + name_compatibility[i]

        if temp_num >= 10:
            temp_num %= 10
        temp.append(temp_num)

    name_compatibility = temp

print(''.join(map(str, name_compatibility)))
