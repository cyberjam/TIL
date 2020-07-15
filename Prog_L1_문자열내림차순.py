# Zbcdefg -> gfedcbZ
# string을 sorted의 reverse param을 사용하여 내림차순으로 정렬후 join을 사용하여 list를 string으로 반환
def solution(s):
    return ''.join(sorted(s,reverse=True)) 
print(solution('Zbcdefg'))


# 다른사람풀이
# 동일.
