
def solution(s):
    answer = ''
    q = len(s)//2
    r = len(s)%2
    if r != 0: # 문자 길이가 홀수일 경우 
        answer=s[q:q+1]
    else:
        answer=s[q-1:q+1]
    return answer
