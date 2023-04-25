# 백준 - 실버5 - 콰트로치즈피자 - 27964 - 단순 구현, 자료 구조(set), 문자열 문제
'''
단순 구현, 자료 구조(set), 문자열 문제

단순 구현 문제이다. 중복되는 값을 제거하기 위해 set을 사용해서 res 변수를 만들었다.
나머지 풀이 과정은 코드를 보면 쉽게 이해할 수 있다.
'''

n = int(input())
toping_list = list(input().split())

# 테스트
# n = 4
# toping_list = [ 'CheddarCheese', 'MozzarellaCheese', 'GoudaCheese', 'GranaPadanoCheese' ] # yummy
# n = 4
# toping_list = [ 'MozzarellaCheese', 'MozzarellaCheese', 'MozzarellaCheese', 'MozzarellaCheese' ] # sad
# n = 4
# toping_list = [ 'CheeseBurger', 'CheeseBall', 'CheeseCake', 'CheeseRavioli' ] # sad
# n = 4
# toping_list = [ 'C', 'Chess', 'cheese', 'Cheesa', 'Cheesz', 'Cheesp', 'Cheese' ] # sad

res = set()

for i in toping_list:
    if 'Cheese' in i[len(i) - 6::]:
        res.add(i)

if len(res) >= 4:
    print('yummy')
else:
    print('sad')
