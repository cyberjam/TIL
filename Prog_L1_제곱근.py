import math
def solution(n):
    root = math.sqrt(n)
    
    return int((root+1)**2) if root == int(root) else -1



# 다른 사람 풀이

def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
    
    
    
# 제곱근이 1/2 제곱과 같구나..
