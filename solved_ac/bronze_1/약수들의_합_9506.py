# 백준 - 브론즈1 - 약수들의 합 - 9506 - 단순 구현, 수학 문제
'''
단순 구현, 수학 문제

문제를 잘 읽어야 된다. n '자신을 제외한 모든 약수의 합'이다. 이걸 생각 안하고 중간에 sum을 통해 n과 같아 졌을 때 출력했었다가 틀렸었다.
입력으로 들어온 숫자를 n라고 하면 n를 제외한 약수 리스트를 구한 다음, 리스트의 전체 합이
n과 같으면 출력 형식에 맞춰 출력하고, n과 다르면 '{n} is NOT perfect.'를 출력하면 된다.
'''

while 1:
    n = int(input())
    temp_list = []
    flag = False

    if n != -1:
        for i in range(1, n):
            if n % i == 0:
                temp_list.append(i)

        if sum(temp_list) == n:
            temp = ' + '.join(map(str, temp_list))
            print(f'{n} = ' + temp)
        else:
            print(f'{n} is NOT perfect.')
    else:
        break
