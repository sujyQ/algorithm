import sys

N, K = map(int, sys.stdin.readline().split())

# simple try
cnt = 0
while N != 1 :
    if N % K == 0 :
        N = int(N/K)
    else : 
        N=N-1
    cnt = cnt + 1

print(cnt)
