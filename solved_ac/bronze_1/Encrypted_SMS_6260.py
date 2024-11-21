# 백준 - 브론즈1 - Encrypted SMS - 6260 - 구현, 문자열 문제
'''
구현, 문자열 문제

문자열을 입력받아 패드에 있는 문자를 왼쪽으로 이동시킨다.

풀이 과정
    1. 패드를 리스트로 저장한다.
    2. 문자열을 입력받아 문자를 패드에 있는 문자로 변경한다.
    3. 문자를 왼쪽으로 이동시킨다.
    4. 결과 출력
'''

pads = [
    "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ",
    "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
]

while True:
    line = input()
    if line == "#":
        break  # 입력이 '#'이면 종료

    res = []
    for position, char in enumerate(line, start=1):
        flag = False # 문자가 패드에 있는지 확인하기 위한 플래그

        for pad_index, pad in enumerate(pads):
            if char in pad:
                char_index = pad.index(char)
                pad_length = len(pad)

                new_char_index = (char_index - position) % pad_length # 현재 위치만큼 문자를 왼쪽으로 이동 (순환적으로)
                new_char = pad[new_char_index]
                res.append(new_char)
                flag = True
                break  # 해당 패드를 찾았으므로 내부 루프 종료

        if not flag:
            # 패드에 없는 문자는 그대로 추가
            res.append(char)

    print(''.join(res))
