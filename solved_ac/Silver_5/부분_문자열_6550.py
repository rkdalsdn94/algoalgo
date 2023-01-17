# 백준 - 부분 문자열 - 실버5 - 6550 - 그리디, 문자열 문제
'''
그리디, 문자열 문제

정답을 출력할 때 첫 글자만 대문자이고, 나머진 소문자로 출력해야 하는데 모두 대문자로 출력해서 틀려놓고 구현에 문제가 있나 싶어서 좀 헤맸다.
아래 내 구현에선 b[i] in a[temp] 를 보면 in 보다는 '==' 로 값을 비교하는게 더 좋아 보인다. (다른 사람의 풀이를 참고했다.)
 ㄴ> 이유는 b[i], a[temp] 둘의 값 모두 한 글자씩 비교한다. 따라서, in 보다는 '==' 로 비교하는게 더 좋아 보인다.

풀이 과정
a, b 라는 이름으로 문자열을 띄어쓰기 기준으로 split 한 후 문자를 입력 받는다. 만약, 값이 안들어오면 exit(0)를 이용해 프로그램을 종료한다.
temp 와 res 각각 숫자(0), boolean(False) 형식으로 정답을 체크할 수 있게 변수를 만든다.
b의 길이만큼 반복하면서 b[i] 의 글자가 a[temp] 같으면 temp 를 증가시키고, temp의 글자가 a와 같아지면 'Yes' 아니면 'No'를 출력한다.


in
    sequence subsequence
    person compression
    VERDI vivaVittorioEmanueleReDiItalia
    caseDoesMatter CaseDoesMatter
out
    Yes
    No
    Yes
    No
'''

while 1:
    try:
        a, b = input().split()
        temp = 0
        res = False

        for i in range(len(b)):
            if b[i] in a[temp]:
            # if b[i] == a[temp]: -> 이 코드가 더 가독성이 좋은거 같다.
                temp += 1

                if temp == len(a):
                    res = True
                    break
        if res:
            print('Yes')
        else:
            print('No')
    except:
        exit(0)
