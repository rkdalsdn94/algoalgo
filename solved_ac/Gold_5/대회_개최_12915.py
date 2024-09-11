# 백준 - 골드5 - 대회 개최 - 12915 - 그리디, 이진 탐색 문제
'''
그리디, 이진 탐색 문제

이진 탐색을 사용하지 않아도 풀리는 문제이다. (이진 탐색을 사용하면 시간이 더 빠름)
 - 사실 이진 탐색의 left, right 값을 어떤 값으로 잡아야 될 지 몰라 그리디하게 먼저 풀어 봤는데 풀렸던 문제이다.
 - 다른 사람의 코드를 참고해보니 left 값은 0으로 right 값은 e, m, h 중 가장 작은 값으로 잡고 푼 코드가 이해가 잘 됐다.
    - 해당 코드는 제일 아래 쪽에 주석으로 달아 놨다. (e, m, h 의 값을 em과 mh를 더한 값으로 수정해야 됨)

가장 쉬운 문제와 어려운 문제는 e와 h를 먼저 확인한 뒤, 값이 없다면 em과 mh를 확인하면 된다.
그리디하게 풀 때 중간 문제를 계산하는 방법을 잘 생각해야 한다.
중간 문제가 없을 때 em과 mh를 사용할 수 있다. 이때 em을 먼저 사용해야 하는데, 이유는 다음과 같다. (최적해를 찾는 방법, ChatGPT)
1. 중간 문제에 mh를 배정하는 경우:
    - mh를 중간 문제에 사용하고 나면 em만 남습니다.
    - em은 중간 문제나 쉬운 문제로 사용할 수 있지만, 어려운 문제에 사용할 수 없기 때문에 어려운 문제에 문제가 배정되지 못합니다.
    - 따라서, 어려운 문제를 충당할 방법이 없어집니다. 이 경우 최적해에 도달하지 못하게 됩니다.
2. 중간 문제에 em을 배정하는 경우:
    - em을 중간 문제에 사용하고 나면 mh가 남습니다.
    - mh는 중간 문제뿐만 아니라 어려운 문제에도 사용할 수 있기 때문에, mh를 어려운 문제에 배정하면 문제를 모두 충당할 수 있습니다.
    - 이 경우에는 중간 문제와 어려운 문제 모두가 배정되어 최적해에 도달할 수 있습니다.
결론:
 - 중간 난이도에 문제를 배정할 때 mh를 아껴두고 em을 먼저 사용하는 것이 중요한 이유는, mh가 어려운 문제에도 사용할 수 있는 유일한 자원이기 때문입니다.
 - 만약 중간 문제에 mh를 먼저 사용하면, 어려운 문제를 충당할 자원이 부족하게 되어 최적해에 도달할 수 없게 됩니다.

코드 진행 과정
    1. e, em, m, mh, h를 입력받는다.
    2. res를 0으로 초기화한다.
    3. 다음을 반복한다.
        3.1. e_flag, m_flag, h_flag를 False로 초기화
        3.2. e가 0보다 크다면 e를 1 감소시키고 e_flag를 True로 바꾼다.
        3.3. e가 0보다 크지 않다면 em을 1 감소시키고 e_flag를 True로 바꾼다.
        3.4. m가 0보다 크다면 m를 1 감소시키고 m_flag를 True로 바꾼다.
        3.5. m가 0보다 크지 않다면 em과 mh 중 큰 값을 1 감소시키고 m_flag를 True로 바꾼다.
            3.5.1. em이 mh보다 크거나 같다면 em을 1 감소시키고 m_flag를 True로 바꾼다.
                 - em을 먼저 감소시키는 이유는 em이 mh보다 크거나 같을 때 em을 감소시키면 mh를 감소시킬 수 있기 때문이다. (최적해를 찾는 방법)
        3.6. h가 0보다 크다면 h를 1 감소시키고 h_flag를 True로 바꾼다.
        3.7. h가 0보다 크지 않다면 mh를 1 감소시키고 h_flag를 True로 바꾼다.
        3.8. e_flag, m_flag, h_flag 중 하나라도 False라면 반복을 종료한다.
        3.9. res를 1 증가시킨다.
    4. res를 출력한다.
'''

e, em, m, mh, h = map(int, input().split())

# 테스트
# e, em, m, mh, h = 2, 2, 1, 2, 2 # 3
# e, em, m, mh, h = 100, 100, 100, 0, 0 # 0
# e, em, m, mh, h = 1, 2, 3, 4, 5 # 3

res = 0

while True:
    e_flag = False
    m_flag = False
    h_flag = False

    if e > 0:
        e -= 1
        e_flag = True
    elif em > 0:
        em -= 1
        e_flag = True

    if m > 0:
        m -= 1
        m_flag = True
    elif em > 0 or mh > 0:
        if em >= mh:
            em -= 1
            m_flag = True
        else:
            mh -= 1
            m_flag = True

    if h > 0:
        h -= 1
        h_flag = True
    elif mh > 0:
        mh -= 1
        h_flag = True

    if not (e_flag and m_flag and h_flag):
        break

    res += 1

print(res)

'''
이진 탐색을 활용한 코드

a, b, c, d, g = map(int, input().split())
e = a+b
m = b +c+d
h = d+g
def f(x):
    global a, b, c, d, g, e, m, h
    p = a+b -x
    if a-x>=0:
        p =b
    q = p+c+d -x
    if p+c -x>=0:
        q = d
    r = q+g -x
    if p>=0 and q>=0 and r>=0:
        return True
    else:
        return False
lt = 0
rt = min(e, m, h)
while lt<=rt:
    mid = (lt+rt)//2
    if f(mid):
        res = mid
        lt = mid +1
    else:
        rt = mid -1
print(res)
'''
