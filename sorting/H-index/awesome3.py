def counting(l, n):
    return len(list(filter(lambda x: x >= n, l)))

def solution(citations):
    answer = 0
    for i in range(max(citations)):
        if counting(citations, i) >= i:
            answer = i
        else:
            break
    return answer