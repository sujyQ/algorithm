def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    patterns = [pattern1, pattern2, pattern3]
    
    answer = []
    for pattern_n, pattern in enumerate(patterns) :
        correct = 0
        for i in range(len(answers)) :
            correct += 1 if pattern[i%len(pattern)] == answers[i] else 0
        if answer :
            max_score = max([ans[1] for ans in answer])
            # print(max_score)
            if max_score < correct :
                answer = []
                answer.append([pattern_n+1, correct])
            elif max_score == correct :
                answer.append([pattern_n+1, correct])
            else :
                pass
        else :
            answer.append([pattern_n+1, correct])
    
    answer = [ans[0] for ans in answer]
    
    return answer