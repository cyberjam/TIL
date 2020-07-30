def solution(strings,n):
    return sorted(sorted(strings),key=(lambda x:x[n]))
        
        
print(solution(['sun', 'bed', 'car'],1))
print(solution(['abce', 'abcd', 'cdx'],2))


# sort 하면 사전식으로 정렬.
# 이후 n 인덱스 기준으로 하면 같더라도 사전식으로 남아 있음
