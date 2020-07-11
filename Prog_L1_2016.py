#주어진 날의 요일을 구하는 문제
#1월 1일의 요일과 년도는 제시
#2016년은 윤년

def solution(a, b):
    #a는 월, b는 일
    #1월 1일은 금요일
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    max_month = [31,29,31,30,31,30,31,31,30,31,30,31] 	 # 각 월의 최대 일수, 2월은 윤년으로 29일 
    return week[(sum([max_month[month] for month in range(a-1)])+b)%7] #기준일 1월1일과 주어진 날짜 5월 24사이 일수를 7로 나눈 나머지 값이 week의 index.

print(solution(5, 24))














