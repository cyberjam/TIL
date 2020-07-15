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

# 다른 사람 코드에 대한 내 풀이 : '%'와 '//'을 설명드리자면 321%10은 123을 10으로 나눈 나머지 3을 반환합니다. 
# 123//10은 123을 10으로 나눈 몫 12를 반환합니다. 따라서 12를 다시 함수에 넣고 돌리겠죠. (return 123%10 + sum_disgit(123//10) -> return 3 + sum_digit(12))
# 2번째 돌릴땐 return에는 이전에 반환한 3 에다가 + 12%10 + sum_digit(12//10). 즉 2번째에는 return 3+2+sum_digit(1)이 됩니다. 
# 3번째에는 if문에서 1이 10보다 작으므로 return 1을 해주고 최종적으로 return 3+2+1이 됩니다.
