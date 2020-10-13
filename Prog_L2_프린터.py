## 스택으로 푸는 문제인데 다른 방향으로 풀어 시간을 허비했다.
# 파이썬 스택 정석으로 사용하는 법을 찾아봐야겠다

# 튜플 2번쨰 원소를 기준으로 최대값을 가진 튜플 2번째 원소 반환
def maxInTuple(lst):
    return max(lst,key=lambda x:x[1])[1] 


def solution(priorities, location):
    answer = 0
    # 대기열 인덱스와 우선순위를 튜플로 묶었다. any 같은 방법으로도 가능한가보다
    wait_prior = [(i,elem) for i,elem in enumerate(priorities)]
    print_prior = []
    
    #대기열이 비어있을 때까지 0번째 원소를 기준으로 스택
    while len(wait_prior):
        #만약 현재 0번째가 대기열에서 우선순위가 가장 높다면
        if wait_prior[0][1]==maxInTuple(wait_prior):
        #프린트 대기열에 pop한 튜플 2번째 원소를 붙여준다
            print_prior.append(wait_prior.pop(0)[0])
        #만약 0번째 우선순위가 높지 않다면
        else:
            # pop한후 다시 뒤에 붙여준다
            wait_prior.append(wait_prior.pop(0))
            
    # 프린트 대기열에서 원하는 인덱스 위치인덱스를 반환한다
    answer = print_prior.index(location)+1
    return answer
    
    
    ## 다른 사람 풀이##########################
    def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        # 지금 pop한 원소가 이후 원소보다 우선순위가 낮다면
        if any(cur[1] < q[1] for q in queue):
        # 대기열 뒤에 붙여준다
            queue.append(cur)
        else:
        #지금 pop한 원소가 이후 원소보다 우선순위가 높다면
            answer += 1 #높은 원소 카운트
            if cur[0] == location: # 만약 궁금해하던 위치라면
                return answer # 그 위치의 대기열 순서를 반환하고 종료
                
     
     # 튜플을 사용했고, 스택을 이용한 점은 같지만
     # location까지만 접근한 점은 효율적으로 잘 만들었다.
     
