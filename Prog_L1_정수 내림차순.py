def solution(n):
    answer = [char for char in str(n)]
    answer = sorted(answer,reverse=True)
    answer = ''.join(answer)
    answer = int(answer)
#     return int(''.join(sorted([char for char in str(n)],reverse=True)))
    return answer

print(solution(118372))



## OUTPUT : 873211
