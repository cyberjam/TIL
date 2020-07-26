def solution(arr):
    answer = []
    if(len(arr) == 1):
        answer.append(-1)
    else:
        arr.remove(min(arr))
        answer = arr[:]
    return answer
    
    
    
#다른사람풀이
def rm_small(mylist):
  return [i for i in mylist if i > min(mylist)] or [-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))
