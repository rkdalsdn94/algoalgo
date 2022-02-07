'''
단순하게 생각하면 아래와 같이 풀 수 있는데, 다른 방식으로 풀어보고 싶어서 다른 풀이를 생각했다.
a_list.extend(b_list)
print(*sorted(a_list))

아래의 코드에서 처음에 pop(0)를 해서 append 하려고 했는데, 시간초과(q였으면 가능 했을거 같다.)가 난다.
당연히 시간초과가 나는게 pop(0)는 O(n) 만큼의 시간이 걸린다 --> 아래 코드로는 O(n^2)이 돼서 시간초과가 난거 같다.
그래서 아래와 같은 방식으로 수정했다.
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# 테스트
# a, b = 2, 2
# a_list = [3, 5]
# b_list = [2, 9] # 2 3 5 9
# a, b = 2, 1
# a_list = [4, 7]
# b_list = [1] # 1 4 7
# a, b = 4, 3
# a_list = [2, 3, 5, 9]
# b_list = [1, 4, 7] # 1 2 3 4 5 7 9
 
a_cnt, b_cnt = 0, 0
res = []

while a_cnt != a or b_cnt != b:
    if a_cnt == a:
        res.append(b_list[b_cnt])
        b_cnt += 1

    elif b_cnt == b:
        res.append(a_list[a_cnt])
        a_cnt += 1

    else:
        if a_list[a_cnt] < b_list[b_cnt]:
            res.append(a_list[a_cnt])
            a_cnt += 1
        else:
            res.append(b_list[b_cnt])
            b_cnt += 1

print(*res)
