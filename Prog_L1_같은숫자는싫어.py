# [1,1,1,3,4,6,6] -> [1,3,4,6]
# 내가 생각해낸 알고리즘은 arr의 해당 인덱스 원소가 바로 뒤 원소와 다를 경우 list에 담는 것이다. 
# 조건에서 원소 범위는 0~9이므로 마지막에 -1을 삽입하여 실제 마지막 원소도 반환가능하도록 만들었다.
# list comprehension으로 구현하여 공간효율성을 조금이라도 높이고자 하였다.
def solution(arr): 
    arr.append(-1) 
    return [ arr[i] for i in range(len(arr)-1) if arr[i] != arr[i+1] ]

# 사실 이전에 코드는 하드코딩 같아 마음에 안들어 제출하기전에 다시 짰다.
# 이전 코드
# 이전 코드 알고리즘은 비어있는 list에 arr 첫번째 원소를 삽입하고, 
# 비어있는 list answer 마지막 원소와 arr 원소를 하나씩 비교하여 없다면 answer에 append 한다.
# def solution(arr):
#     answer = [arr[0]]
#     for elem in arr[1:]:
#     	if answer[-1]!=elem:
#     		answer.append(elem)
#     return answer
    
    
    
