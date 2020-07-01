def solution(a, b) :
    answer = 0
    if a > b :
        for i in range(b, a+1)  :
            answer += i
    elif a == b :
        answer = a
    else:
        for i in range(a,b+1)  :
            answer += i

    return answer
    
    
    
    #다른사람 풀이
    
def sol(a,b):
    if a>b: a,b = b,a     #a가 b보다 클경우 서로 바꿔줌
    return sum(range(a,b+1)) #range도 sum이 
