def solution(arr, divisor):
    answer = sorted([elem for elem in arr if not elem%divisor])
    if not len(answer):
        return [-1]
    else:
        return answer
        
        
        
# 다른사람 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]


# or이라니.... sorted([n for n in arr if n%divisor == 0]) 값이 없다면 NONE
# NONE or [-1] 이라면 [-1] 호출

# 값이 있다면
# [1,2,3] or [-1] 에서 [1,2,3] 까지만 호출
