'''
문제 난위도는 높지 않은데 코드를 좀 더 깔끔하게 짜고 싶어서 고민을 좀 했었다.
map함수를 최대한 활용해 보려고 했었다. 여기서 더 최적화 할 수 도 있을거 같은데,
현재 내 가독성면에서 지금이 제일 깔끔해서 이렇게 만들었다.
---> 만약 map(함수, 이터러블)에서 함수가 인자가 2개 이상이면 itertools를 import하고 starmap을 사용하면 2개 이상의 인자도 가능하다.
'''

def dp(n):
    return n + sum(map(int, str(n)))

ck = set(map(dp, range(1, 10001) ))

for i in range(1, 10001):
    if i not in ck:
        print(i)
