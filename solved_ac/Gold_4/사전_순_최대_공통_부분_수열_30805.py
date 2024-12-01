# 백준 - 골드4 - 사전 순 최대 공통 부분 수열 - 30805 - 그리디 문제
'''
그리디 문제

최대 공통 부분 수열 찾기: 두 수열에서 공통으로 등장하는 가장 큰 값을 찾아 나감. (그리디 접근법)
재귀적 접근: 가장 큰 값을 찾으면 그 값을 결과에 추가하고, 그 이후의 부분 수열에 대해 다시 같은 작업을 반복한다.
탐색 및 제거: 각 단계마다 가장 큰 값을 찾고, 해당 값을 제거하면서 다음 단계로 넘어감.
종료 조건: 어느 한 수열이 빈 리스트가 되면 종료.

풀이 과정
    1. 두 배열을 입력 받는다.
    2. 두 배열에서 가장 큰 값과 그 인덱스를 찾는다.
    3. 두 값이 같으면 결과에 추가하고 그 이후 부분으로 재귀 호출한다.
    4. 두 값이 다르면 더 큰 값을 가진 배열에서 해당 값을 제거하고 재귀 호출한다.
    5. 두 배열 중 하나라도 비어 있으면 결과를 반환한다.
    6. 비어 있지 않다면 3번으로 돌아가서 반복한다.
'''

def recursive(n_list, m_list, res = []):
    if (not n_list) or (not m_list):
        return res

    tmp1, tmp2 = max(n_list), max(m_list)
    idx1, idx2 = n_list.index(tmp1), m_list.index(tmp2)

    if tmp1 == tmp2:
        res.append(tmp1)
        return recursive(n_list[idx1 + 1:], m_list[idx2 + 1:], res)
    elif tmp1 > tmp2:
        n_list.pop(idx1)
        return recursive(n_list, m_list, res)
    else:
        m_list.pop(idx2)
        return recursive(n_list, m_list, res)

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 테스트
# n = 4
# n_list = [1, 9, 7, 3]
# m = 5
# m_list = [1, 8, 7, 5, 3] # 2  \  7 3

res = recursive(n_list, m_list)

print(len(res))
if res:
    print(*res)
