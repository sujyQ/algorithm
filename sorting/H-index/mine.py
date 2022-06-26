def solution(citations):
    sorted_cit = sorted(citations, reverse = True)
    answer = 0

    max_cit = sorted_cit[0]
    for i in range(max_cit, 0, -1) :
        _cits = [1 if _cit >= i else 0 for _cit in sorted_cit]
        # print(_cits, sum(_cits))
        if sum(_cits) >= i :
            answer = i
            break


    return answer