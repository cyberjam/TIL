a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*"*a)





# 다른사람 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)


#우와 for 없이//
