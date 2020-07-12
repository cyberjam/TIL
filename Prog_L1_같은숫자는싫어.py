# [1,1,1,3,4,6,6] -> [1,3,4,6]
# 전체 구조는 해당 인덱스 원소가 바로 뒤 원소와 다를 경우 list에 담는 것이다. 
# 조건에서 원소 범위는 0~9이므로 마지막에 -1을 삽입하여 실제 마지막 원소도 반환가능하도록 만들었다.
def solution(arr): 
    arr.append(-1) 
    return [ arr[i] for i in range(len(arr)-1) if arr[i] != arr[i+1] ]
    
    
    
