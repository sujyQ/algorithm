
N = int(input())

cnt = 0

for hour in range(0, N+1) :
    for min in range(0, 60) :
        for sec in range(0, 60) :
            if str(sec).count('3') + str(min).count('3') + str(hour).count('3') >= 1:
                cnt += 1

print(cnt)

cnt = 0

# simpler if condition
for hour in range(0, N+1) :
    for min in range(0, 60) :
        for sec in range(0, 60) :
            if '3' in str(sec) + str(min) + str(hour) :
                cnt += 1

print(cnt)