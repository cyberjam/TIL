def solution(d, budget):
    answer = 0
    for dep in sorted(d):
        budget-=dep
        if budget>=0:
            answer+=1
            
        
    return answer
