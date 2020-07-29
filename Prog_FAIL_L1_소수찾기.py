#친구 repo 코드 
#https://github.com/cyberjam/Programmers/blob/master/%EB%82%B4%EA%B0%80%20%ED%92%80%EC%96%B4%EB%B3%B8%20%EB%8B%B5%EC%95%88/%EC%86%8C%EC%88%98%20%EC%B0%BE%EA%B8%B0%20(10.17%2C%20%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C%2C%20Level_1).ipynb


def solution(n):
	num=set(range(2,n+1))    # set 연산을 위해
	for i in range(2,int(n**0.5)+1):      sqrt(n)까지만 순회 O(sqrt(n))
	    if i in num: 
	    	num-=set(range(2*i,n+1,i))   
        # 가장 대단. 1. for 사용하지 않은점. 2. 효율적인 순회 : n=2일 때 2배수 삭제. n=3일때 2일때 이미 지운 6 뛰어넘고 3씩 9부터 순회.
	return len(num)


print(solution(47))




# 위 코드대로라면 소수인지 확인할 필요가 없다


#참고
#에라토스테네스의 체(https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)

### 내코드





### 내코드2
def isPrime(num):
	for i in range(2,int(num**(1/2))+1):
		if num%i==0:
			return False
	return num


def solution(endnum):
	num = list(range(2,endnum+1))

	for n in range(2,int(len(num)**(1/2))+1):
		if isPrime(n)!=False: # 소수라면
			for rm in range(2,endnum//n+1):
				print(n,n*rm)
				if n*rm in num:
					num.remove(n*rm)

	return len(num)

print(solution(5))
