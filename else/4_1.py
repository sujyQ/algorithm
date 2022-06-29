import sys

###### my answer

N = int(sys.stdin.readline())
plan = sys.stdin.readline().split()

L_cnt = plan.count('L')
R_cnt = plan.count('R')
U_cnt = plan.count('U')
D_cnt = plan.count("D")

pos = [1,1]

for i in plan :
    if i == 'L' and pos[0] > 1:
        pos[0] -= 1
    elif i == "R" and pos[0] < N :
        pos[0] += 1
    elif i == "U" and pos[1] > 1 :
        pos[1] -= 1
    elif i == "D" and pos[1] < N :
        pos[1] += 1
        

print(pos[1], pos[0])


##### answer example

n = int(input())
x, y = 1, 1
plans = input().split()

# moving directions according to L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moving_types = ['L', 'R', 'U', 'D']

# check moving plans one by one
for plan in plans :
    for i in range(len(moving_types)) :
        if plan == moving_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n :
            continue
        x, y = nx, ny

print(x, y)