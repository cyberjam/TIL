def solution(s):
    answer = ''
    a = [int(num) for num in s.split()]
    answer = str(min(a)) + ' ' + str(max(a))
    return answer
    
    
    
    
def solution(s):
    answer = ''
    a = list(map(int,s.split()))
    answer = str(min(a)) + ' ' + str(max(a))
    return answer
