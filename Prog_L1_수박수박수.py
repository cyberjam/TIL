# 내풀이
def solution(n):
    return ('수박'*(n//2+1))[:n] # 무한하게 수박을 반복하는게 공간효율적으로 낭비 같아 (n//2+1)로 했다. 

#좀더 효율적인 코드를 생각하고 싶다 예를 들면 중간 수 가져오기 같은것

    
# 다른 사람 풀이

def water_melon(n):
    s = "수박" * n
    return s[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));




# 오 대박 처음으로 베스트 코드를 이겼다 근소하지만.



# 다른사람 풀이2
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));

#이게 더 효율적


#친구 풀이3
# https://github.com/cyberjam/Programmers/blob/master/%EB%82%B4%EA%B0%80%20%ED%92%80%EC%96%B4%EB%B3%B8%20%EB%8B%B5%EC%95%88/%EC%88%98%EB%B0%95%EC%88%98%EB%B0%95%EC%88%98%EB%B0%95%EC%88%98%EB%B0%95%EC%88%98%EB%B0%95%EC%88%98%20(10.18%2C%20%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C%2C%20Level_1).ipynb
# index와 %연산자를 잘 이용한 예


