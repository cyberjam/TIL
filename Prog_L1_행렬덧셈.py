def solution(arr1, arr2):
    return [[arr1[a1][a2] + arr2[a1][a2] for a2 in range(len(arr1[a1]))] for a1 in range(len(arr1))]


    # for i in range(len(arr1)):
    # 	for j in range(len(arr1[i])):
    # 		arr2[i][j]=arr1[i][j]+arr2[i][j]



#다른사람풀이

def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
