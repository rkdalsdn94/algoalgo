def solution(numbers, hand):
    answer = ''
    left, right = [1,4,7], [3,6,9]
    dic = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2),
    }
    l_cur, r_cur = '*', '#'
    
    for i in numbers:
        if i in left:
            answer += 'L'
            l_cur = i
        elif i in right:
            answer += 'R'
            r_cur = i
        else:
            l_ck = abs(dic[i][0] - dic[l_cur][0]) + abs(dic[i][1] - dic[l_cur][1])
            r_ck = abs(dic[i][0] - dic[r_cur][0]) + abs(dic[i][1] - dic[r_cur][1])
            if l_ck < r_ck:
                answer += 'L'
                l_cur = i
            elif l_ck > r_ck:
                answer += 'R'
                r_cur = i
            else:
                if hand == 'left':
                    answer += 'L'
                    l_cur = i
                else:
                    answer += 'R'
                    r_cur = i
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL") # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")  # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")    # "LLRLLRLLRL"