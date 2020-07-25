import math
def solution(n, m):
    return [math.gcd(n,m),(n*m) / math.gcd(n,m)]



# 다른 사람 풀이
# 유클리드 호제법
# 담백하다


def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))
