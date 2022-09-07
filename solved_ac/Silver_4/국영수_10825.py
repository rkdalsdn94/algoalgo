# 백준 - 국영수 - 10825 - 실버4 - 정렬 문제
'''
정렬 문제

문제에 주어진 순서대로 정렬해서 풀면 된다. (아래 순서)

1. 국어 점수가 감소하는 순서로 -> lambda에서 1번째
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로 -> lambda에서 2번째
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로 -> lambda에서 3번째
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 -> lambda에서 마지막
   - (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
'''

n = int(input())
class_student = sorted([ list(input().split()) for _ in range(n) ], key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 테스트
# n = 12
# class_student = sorted([
#     ['Junkyu' ,'50', '60', '100'],
#     ['Sangkeun', '80', '60', '50'],
#     ['Sunyoung', '80', '70', '100'],
#     ['Soong', '50', '60', '90'],
#     ['Haebin', '50', '60', '100'],
#     ['Kangsoo', '60', '80', '100'],
#     ['Donghyuk', '80', '60', '100'],
#     ['Sei', '70', '70', '70'],
#     ['Wonseob', '70', '70', '90'],
#     ['Sanghyun', '70', '70', '80'],
#     ['nsj', '80', '80', '80'],
#     ['Taewhan', '50', '60', '90']
# ], key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
'''
out
    Donghyuk
    Sangkeun
    Sunyoung
    nsj
    Wonseob
    Sanghyun
    Sei
    Kangsoo
    Haebin
    Junkyu
    Soong
    Taewhan
'''

for i in class_student:
    print(i[0])
