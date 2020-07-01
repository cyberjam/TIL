
def solution(s):
    answer = ''
    q = len(s)//2
    r = len(s)%2
    if r != 0: # 문자 길이가 홀수일 경우 
        answer=s[q:q+1]
    else:
        answer=s[q-1:q+1]
    return answer

#다른사람 풀이

def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1] # //가 -,+ 보다 우선순위가 높다. 길이가 홀수든 짝수든 가능 # 변수 할당없이 대단
