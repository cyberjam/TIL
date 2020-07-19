#https://github.com/KoEonYack/LevelUp-Algorithm/blob/master/Programmers/Level_1/Prog_%EC%B2%B4%EC%9C%A1%EB%B3%B5_2.py

def solution(n, lost, reserve):
    reserveD = [x for x in reserve if x not in lost] # 중복 제거
    lostD = [x for x in lost if x not in reserve] # 중복 제거

    for server in reserveD:
    	if server-1 in lostD:# 앞에 친구가 여벌이 있는 경우
    		lostD.remove(server-1)
 
    	elif server+1 in lostD: # 뒤에 친구가 여벌이 있는 경우
    		lostD.remove(server+1)
 
    	elif server in lostD: # 체육복 여벌을 가져온 사람. 앞에서 중복 제거 했으니 필요없음 
    		lostD.remove(server)

    return n-len(lostD)

# print(solution(5,[2, 4],[1, 3, 5]))
# print(solution(5,[2, 4],[3]))
# print(solution(3,[3],[3,1]))
print(solution(3,[3,7],[3,5]))


# 다른사람 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

