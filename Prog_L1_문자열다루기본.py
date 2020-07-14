# 길이가 4또는 6이며 문자열이 모두 숫자일경우 True 아닐경우 False 반환.
# 문제에서 명시하지는 않았지만 길이가 4 또는 6이 아닐경우 False
def solution(s):
    return True if ((len(s)==4)|(len(s)==6)) & (len([c for c in s if (c>chr(47)) & (c<chr(58))])==len(s)) else False
# C언어에서 아스키코드로 풀었던게 기억.
# 연산자 ==이 | 보다 우선순위가 높아 ()를 해줘야한다.

#다른 사람 풀이

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
    
    #len(s) in (4, 6) 길이가 4나 6이라면 True.
    #s.isdigit() 문자열내 숫자가 있을 경우 True
    #True & True = True
    
    # s.isdigit()은 filter를 사용해서 풀까 했는데 아스키코드로 하는게 더 효율 높을듯해서 아스키 사용.
    # len(s) in (4, 6)이 인상깊음
