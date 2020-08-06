def solution(n, arr1, arr2):
    # arr1과 arr2의 원소를 순서쌍 tuple로 만들어 i,v로 unpacking
    # i와 v를 union 하고 앞에 빈칸만큼 0으로 채워줌
    # #은 1로 0은 빈칸으로. # 다른 사람 풀이는 rjust를 사용하였다.
    
    answer = [('0'*(n-len(bin(i|v)[2:])))+bin(i|v)[2:] for i,v in list(zip(arr1,arr2))]
    return [inner.replace('1','#').replace('0',' ') for inner in answer]
    
    
print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))


#output:
#['#####', '# # #', '### #', '#  ##', '#####']
#['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']




# 다른 사람 풀이

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
