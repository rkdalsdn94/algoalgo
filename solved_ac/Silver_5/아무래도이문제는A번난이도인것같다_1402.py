# 백준 - 실버5 - 아무래도이문제는A번난이도인것같다 - 1402 - 수학, 애드 훅, 해 구성하기 문제
'''
수학, 애드 훅, 해 구성하기 문제

애드 훅 문제는 답을 구하는 방식이 특이한 문제가 많다...

이 문제는 다음과 같이 생각하면 된다. (ChatGPT)
 - 이 문제에서 항상 “yes”를 출력하면 되는 이유는, 주어진 변환 규칙을 통해 모든 정수 A는 궁극적으로 1로 변할 수 있기 때문입니다.
 - 이는 소인수 분해를 통해 각 인수들의 합으로 변환해 나가는 과정에서 필연적으로 발생하는 결과입니다.
이유를 단계별로 살펴보면:
1. 소인수 분해의 특성:
    어떤 정수 A를 소인수 분해하면, A를 구성하는 소수들의 곱으로 나타낼 수 있습니다.
    예를 들어, 12 = 2 * 2 * 3입니다. 이를 인수들의 합으로 바꾸면 2 + 2 + 3 = 7이 됩니다.
    이처럼 숫자가 점점 작아지는 경향을 보입니다.
2. 계속되는 감소:
    이 과정을 반복하면, 숫자가 계속해서 줄어들게 됩니다.
    언젠가는 A가 더 이상 나누어질 수 없는 1에 도달하게 됩니다.
    예를 들어:
        A = 12 → 7 → (소인수 분해가 안 되므로 더 이상 변환되지 않음)
        A = 6 → 5 → (소인수 분해가 안 되므로 더 이상 변환되지 않음)
3. 모든 수는 1로 변환 가능:
    결국 이 변환 과정을 통해, A가 1로 수렴할 수 있습니다.
    그리고 문제에서는 A가 B로 변환될 수 있는지 묻고 있는데, B는 언제나 A가 수렴할 수 있는 값 중 하나일 수 있습니다.
    특히, 1로 가는 과정에서 중간에 어떤 B가 나오더라도, 항상 B로 변환 가능하다는 의미입니다.
결론:
A는 결국 항상 B로 변할 수 있습니다. 특히, 변환 중간에 거치는 모든 값들 중 B가 있을 수 있으므로, 어떠한 경우에도 “yes”가 답이 됩니다.

풀이 과정
    1. t를 입력받는다.
    2. t만큼 a, b를 입력받는다.
    3. yes를 출력한다.
'''

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print('yes')
