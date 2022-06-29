count = []

def getCount(numbers, target, total, level) :
    # print(numbers, target, total, level)
    if level == len(numbers) :
        if total == target : 
            count.append(1)
    else :
        getCount(numbers, target, total+numbers[level], level+1)
        getCount(numbers, target, total-numbers[level], level+1)

def solution(numbers, target):
    getCount(numbers, target, 0, 0) 
    return len(count)