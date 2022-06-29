from itertools import permutations

def isPrime(num) :
    if num == 1 or num == 0 :
        return False
    
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True

def getInt(num_ch) :
    num_str = ""
    for n in num_ch :
        num_str += n[0]
    return int(num_str)

def solution(numbers):
    answer = 0
    permutation_list = []
    for l in range(len(numbers)) :
        permutate = list(permutations(numbers, l+1))
        for tup in permutate :
            permutation_list.append(getInt(tup))
    
    answer_list = []
    while permutation_list :
        num = permutation_list.pop(0)
        if all(ans != num for ans in answer_list) :
            if isPrime(num) :
                answer_list.append(num)
    return len(answer_list)