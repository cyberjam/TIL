#완주하지 못한 선수

def todict(lst): # 중복 횟수를 세어 딕셔너리로 반환
    dic_1={}
    for elem in lst:
        if elem in dic_1: # 만약 중복이라면
            dic_1[elem]+=1 # 1 증가
        else:
            dic_1[elem]=1 # 1 대입
    return dic_1 # 딕셔너리 반환

dct_part= todict(participant) #참여자 중복 횟수 딕셔너리
dct_comp= todict(completion) # 경기자 중복 횟수 딕셔너리

for elem in dct_comp: # 참여자 횟수에서 경기자 횟수 빼기 -> 경기에 참여하지 않은 동명이인 
    dct_part[elem]-=dct_comp[elem]

answer= [elem for elem in dct_part if dct_part[elem]>0][0]
print(answer)