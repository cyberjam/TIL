# heapq를 사용해보는 문제
# 처음에는 list로 pop insert 하려고 했지만 효율성 0
# heapq는 오름차순으로 정렬된 자료구조기때문에 index 0은 최소라는것을 이용
# list comprehension으로 하나하나 확인하는 것보다 효율성이 높아진다! 

##################################heapq#########################################
# import heapq # heapq는 내장함수
# heapq.heapify(list) # 리스트를 heapq로 변환
# heapq.heappop(heapq_list) # heapq pop 0 index를 pop
# heapq.heappush(heapq_list,willPushValue) # heapq push 0 index push

############################# My Code######################################

import heapq
def scov_func(scoville):
    sco_0 = heapq.heappop(scoville)
    sco_1 = heapq.heappop(scoville)
    result = sco_0 +(sco_1*2)
    heapq.heappush(scoville,result)
    return scoville

# def isUp(scoville,K): # 비효율적
#     return len(scoville)== len([elem for elem in scoville if elem >=K])

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K:
    #while not isUp(scoville,K):
        # 조건에 따라 더이상 갈때까지 가더라도 K이상으로 만들수 없는 경우 -1을 반환해준다
        if len(scoville)<2: 
            return -1
        scov_func(scoville)
        answer+=1   

    return answer
