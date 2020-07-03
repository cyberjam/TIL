# 내 코드
def solution(num):
    return "Even" if num%2==0 else "Odd" # 나머지가 0일경우 Even 이외에는 Odd
    
    
# 다른사람 코드

def evenOrOdd(num):
    if (num%2): # 홀수라면 나머지가 1 -> True
        return "Odd"
    else:
        return "Even"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))


# 내 코드 개선

def solution(num):
    return "Odd" if num%2 else "Even" # 나머지가 1일경우 Odd 이외에는 Even. 완전 깔끔
