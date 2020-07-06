def solution(answers):
    students={2:([2, 1, 2, 3, 2, 4, 2, 5]*(len(answers)//8))+[2, 1, 2, 3, 2][:len(answers)%8],1:([1, 2, 3, 4, 5]*(len(answers)//5))+[1, 2, 3, 4, 5][:len(answers)%5],  3:([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len(answers)//10))+[3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:len(answers)%10]} 
    return sorted([key for key,elem in {key:[i[1]-i[0] for i in zip(answers,val)].count(0) for key,val in students.items()}.items() if elem==max({key:[i[1]-i[0] for i in zip(answers,val)].count(0) for key,val in students.items()}.values())])

# 다른풀이들 보니까 한줄코딩 너무들 하시길래 해봤는데 한줄은 너무하다싶어서 두줄로.
# students 길이 자르는 건 앞에 풀었던 수박수박 다른풀이를 응용하였다.
