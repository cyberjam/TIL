#K번째수
def solution(array, commands):
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]  #i는 중첩리스트 내부 리스트, sorted는 정렬된 결과를 반환, [i[2]-1]는 정렬후 몇번째
# input 형식
# [2,5,1] 2번째에서 5번째까지 잘라 정렬후 1번째
