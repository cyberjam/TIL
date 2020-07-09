def solution(n):
    if not n:#만약 0일경우
        return 0
    elif n==1:#만약 1일경우
        return 1
    else:
        return sum([i for i in range(2,n//2+1) if not n%i]) + n + 1 # 모든 수는 1과 자기자신을 약수로 하니 무조건 더함. 절반넘어서는 검사할 필요 없음
        
        
  #input이 0부터 3000이하.
  
  
  
#다른 사람 풀이

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
    
#다른 사람 풀이2
def sumDivisor(num):
    return sum(filter(lambda x: num % x == 0, range(1, num + 1)))
