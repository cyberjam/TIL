def solution(s):
     return True if len([char for char in s if char == "P" or char == "p" ])==len([char for char in s if char == "Y" or char == "y"]) else False

    
print(solution("pPPYYY"))
print(solution("aaaa"))
print(solution("a"))



#문제를 Pp와 Yy를 합해 짝수인지 물어보는줄 알았으나 Pp 와 Yy 개수가 같은지 물어보는 문제.




# 다른사람풀이
# 모두 소문자로 만들어 count()를 썼다.

def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
