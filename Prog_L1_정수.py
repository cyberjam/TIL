def solution(s):
    return int(s)
    
    
    
#다른사람

def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]): 
    # enumerate로 인해 idx는 index를 number는 str값을 넘겨줌. str[::-1]로 인해 순서가 뒤바뀜
    #4321-
        if number == '-':#마지막 부호수는 음수일경우 음수화
            result *= -1
        else: #숫자를 십진수로 적재
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));

# 위 코드는 디지털공학적으로 잘 설계했지만, 결국 int()를 사용해야하는건 마찬가지이므로 효율성이 떨어진다.
# 하지만 문제 조건이 더러울경우 잘 튜닝해서 쓸만하겠다.
