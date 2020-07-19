def solution(p_num):
    return p_num.replace(p_num[:-4], len(p_num[:-4]) * "*")
    
    
# 뒤 4자리 빼고 모두 *로 가리기

print(solution("01033334444"))
print(solution("027778888"))
