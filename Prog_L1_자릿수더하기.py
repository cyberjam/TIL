def solution(n):
    return sum([int(i) for i in str(n)])
    
    
    
# 다른 사람풀이
# 재귀 대박..

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));


# 1의 자리가 아니라면 return에 10을 나눈 나머지 1의 자리를, 10으로 나눈 몫은 다시 함수에 돌린다. 
# 1의 자리만 남을때까지 돌리고 
# 1의 자리일때는 1의 자리 return하면 마지막에 더해진다.
# 따라서 return 3 + 2 + 1
# 멋지구만
