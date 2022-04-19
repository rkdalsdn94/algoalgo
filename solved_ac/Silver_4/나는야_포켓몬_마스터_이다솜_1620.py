'''
자료 구조 문제

in
    26 5
    Bulbasaur
    Ivysaur
    Venusaur
    Charmander
    Charmeleon
    Charizard
    Squirtle
    Wartortle
    Blastoise
    Caterpie
    Metapod
    Butterfree
    Weedle
    Kakuna
    Beedrill
    Pidgey
    Pidgeotto
    Pidgeot
    Rattata
    Raticate
    Spearow
    Fearow
    Ekans
    Arbok
    Pikachu
    Raichu
    25
    Raichu
    3
    Pidgey
    Kakuna
out
    Pikachu
    26
    Venusaur
    16
    14

처음에 문제를 보고 당황했다...
입력 부분에 대해서 다 읽고 난 후에는 쉽게 풀 수 있었다. dict만 잘 사용하면 된다.
처음 입력 값을을 입력 받으면서 dict에다 문자열로 1, 1의 문자열 이런식으로 만든 후에
나중에 test로 들어온 값들만 출력하면 된다. -> 문자, 숫자 다 입력 받아놔서 test가 문자인지 숫자인지만 검사하면 된다.
1보다 크거나 같다해서 dic의 숫자 부분은 1 부터 시작할 수 있게 range를 잡았다.

기본 python3로 하면 시간초과가 난다. input을 sys로 사용하거나 pypy3로 제출해야 된다.
'''

n, m = map(int, input().split())
dic = dict()

for i in range(1, n + 1):
    monster = input()
    dic[i] = monster
    dic[monster] = i

for _ in range(m):
    test = input()

    if test.isalpha():
        print(dic[test])
    else:
        print(dic[int(test)])
