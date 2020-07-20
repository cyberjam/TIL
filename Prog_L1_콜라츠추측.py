#1-1. 입력된 수가 짝수라면 2로 나눕니다. 
#1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
#2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 8번

def solution(num):
    c = 0
    for count in range(500):
        c=count
        if num==1:
            break
        num = [num/2,num*3+1][int(num%2)] #짝수일때는 리스트의 0인덱스를, 홀수일때는 1인덱스.
    return c if num==1 else -1
    
    
# 다른 사람 풀이는 하드코딩
# num 은 1이상  8000000 미만이므로 1일때 1번으로 결과가 나오는 오류가 있다.
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))


# 참고해서 수정한 내코드
def solution(num):
    for count in range(500):
        if num==1:
            return count
        num = [num/2,num*3+1][int(num%2)]
    return -1
# num==1 조건문을 앞에 둬서 1일때 오류가 없다
    

    
    
