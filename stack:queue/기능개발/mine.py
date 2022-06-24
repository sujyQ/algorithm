def solution(progresses, speeds):
    needs = []
    for progress, speed in zip(progresses, speeds) :
        need = (100 - progress) // speed
        if (100 - progress) % speed > 0 :
            need += 1
        needs.append(need)
    print(needs)
    
    answer = []
    while len(needs) > 0 :
        need = needs.pop(0)
        cnt = 1
        while len(needs) > 0 and need >= needs[0] :
            cnt += 1
            needs.pop(0)
        answer.append(cnt)