import sys

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

