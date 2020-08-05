# 문제를 이해하는데 조금 오래걸렸지만
# 하드코딩

# /연산자가 있는데 뭔가 풀린다 싶으면 zero divide error를 염두하자


def solution(N, stages):
    ptnt_len = len(stages)
    answer = []
    for stg in range(1,N+1):
        if stages.count(stg): #count한 값 0이 아니라면
            answer.append([stages.count(stg)/ptnt_len,stg]) #실패율과 스테이션 
            ptnt_len -= stages.count(stg) # 분모 빼주기
        else: # 0 이라면
            answer.append([0,stg])
            ptnt_len -= stages.count(stg) # 이제 생각해보니 필요없음

    answer_sort = sorted(sorted(answer,key=lambda idx: idx[1]),key=lambda idx:idx[0],reverse = True) 
    # idx 오름차순 정렬후 값 내림차순정렬

    return [idx[1] for idx in answer_sort]  #idx만 추출
