
x의 숫자들 합한 값으로 x를 나눴을때 떨어지는 숫자를 하샤드.

def solution(x):
    return True if not x%sum([int(i) for i in str(x)]) else False


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(18))



# 다른 풀이
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))


# 하 거의 같은데 
