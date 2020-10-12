# 내 풀이
# stack으로 풀고자 하였다.
# pop index  오류에서 당황

def solution(progresses, speeds):
    progresses.reverse() # pop할때 순서때문 # python list는 기본적으로 deque인가보다
    speeds.reverse()
    days = []
    while progresses[-1]!=100: # 마지막 elem이 100이 아니라면 반복
        progresses = [100 if elem+speeds[i]>100 else elem+speeds[i] for i,elem in enumerate(progresses)] # 비효율적이라 마음에 들지 않는다
        print(progresses)
        day=0
        while progresses[-1]==100: # 마지막 elem이 100이라면 모두 pop
            progresses.pop()
            day+=1 # pop한 만큼 count
            if len(progresses)==0: # index error를 위해
                break
            print(progresses)
        if day!=0:
            days.append(day) 100이 있을때만 count 개수를 days에 병합
        if len(progresses)==0:
            break
    answer = days
    return answer
    
    
    # 다른 사람 풀이인데 문제가 개편되어 같은 문제인지 봐야겠다
    
 
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
