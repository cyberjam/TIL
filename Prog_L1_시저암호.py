# 문제 오류 있습니다.
# 여러 공백은 1개의 공백으로 처리된다는 조건은 테스트 케이스에서 고려하지 않았습니다.
# 따라서 여러 공백을 1개의 공백으로 처리하면 오답입니다.

def solution(s, n):
	return "".join([" " if char==" " else chr(ord(char)+n-26*int((ord(char)+n)/(90+1))) if char.isupper() else chr(ord(char)+n-26*int((ord(char)+n)/(122+1))) for char in s])
  
  
# 다른 사람 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
