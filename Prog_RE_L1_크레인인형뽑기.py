# 중복 숫자 제거가 어려웠다.
# 꼭 다시볼것

def dup_del(lstSelct):

    lstSelct.append(-2) # 인덱스 오류 방지로 마지막 -2 추가
    for idx in range(len(lstSelct)-1): 
        if lstSelct[idx]==lstSelct[idx+1]: # 같은 숫자 2개가 있다면 모두 -1로 바꿈
            lstSelct[idx]=-1
            lstSelct[idx+1]=-1

    if -1 in lstSelct: # 리스트에 -1이 있다면 
        while -1 in lstSelct: # -1이 없어질때지 없앰
            lstSelct.remove(-1)
        return dup_del(lstSelct) #다시 회귀
    lstSelct.remove(-2) # 같은 숫자도 없으니 리스트에 -1도 없고 -2 때어줌
    return lstSelct


def solution(board, moves):
    answer = 0
    # 행렬 전치
    board_edit = [[board[j][i] for j in range(len(board))[::-1] if board[j][i]] for i in range(len(board[0]))] 
#     print(board_edit)
    #추출한 원소 list로 (0제외)
    lstSelct=[board_edit[lst-1].pop() for lst in moves if board_edit[lst-1]]
#     while dup_del(lstSelct)!=False:


    return len(lstSelct)-len(dup_del(lstSelct)) # 중복 인형 터진 개수를 구하는 거니 원래에 중복 없앤 리스트 숫자 뺌
    
    
    
# 하드코딩..


#다른 사람풀이
# 스택을 구현했다고 하는데 

def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
