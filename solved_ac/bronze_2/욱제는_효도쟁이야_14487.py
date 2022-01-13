'''
원래 문제 이름는 욱제는 효도쟁이야!! 라는 이름을 사용하고 있는데,
터미널(iterm2)에서 python 파일경로  <-  이렇게 실행했을 때에는 문제 없이 동작하지만,
vscode 내에서 cmd + shift + D 를 사용해서 실행 시켰을때 파일 제목에 특수문자(!!) 때문인지 동작을 안한다.
ㄴ>  FileNotFoundError: [Errno 2] No such file or directory: ~~~~~/algoalgo/solved_ac/bronze_2/욱제는_효도쟁이야python
   (위와 같은 식으로 오류를 뿜어서 느낌표를 빼고 시도하니까 정상 동작함).
사실 파일 이름에 특수문자를 포함시킬 일이 없어서 처음에 당황했었다.. (위 문제처럼 파일 이름내에 !표가 들어가거나 할 일이 없다..)

문제는 너무 단순했다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [1,6,5,2,4] # 12
# n = 4
# n_list = [100,100,100,101] # 300

print(sum(n_list) - max(n_list))