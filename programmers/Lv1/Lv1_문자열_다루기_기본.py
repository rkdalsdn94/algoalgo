def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False

# 다른 사람 풀이 보니까 이 밑에 방법이 더 좋아보임..
# def solution(s):
#     return s.isdigit() and len(S) in (4, 6)
