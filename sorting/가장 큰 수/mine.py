def getNth(num_str, n) :
    nth = -1
    cnt = 0
    while len(num_str) > 0 :
        if len(num_str)  > 1 :
            nth = int(num_str) // 10**(len(num_str) - 1)
            num_str = num_str[1:]
            cnt += 1
            if cnt == n :
                break
        else :
            nth = int(num_str)
            break
    return nth
        

def solution(numbers):
    numbers = sorted([str(num) for num in numbers], reverse=True)
    for i, (num_str, next_num_str) in enumerate(zip(numbers, numbers[1:])) : 
        if getNth(num_str, 1) == getNth(next_num_str, 1) :
            if len(num_str) > len(next_num_str) :
                numbers[i], numbers[i+1] = next_num_str, num_str
    answer = ''
    for num in numbers :
        answer += num
    return answer