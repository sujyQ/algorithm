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

# second one
N, K = map(int, sys.stdin.readline().split())

cnt = 0
while True :
    target = (N//K)*K       # target은 N 이하의 수 중 최대인 K의 배수
    cnt += (N-target)       # cnt은 N과 target의 차이 : 1씩 빼기
    N = target              # N은 K로 나누어 떨어지는 수가 됨

    if N < K :
        break

    cnt += 1                # K로 나누기
    N //= K

cnt += (N-1)                # N이 K보다 작은 값일 때 1씩 빼기
print(cnt)

# test case : N = 25, K = 3
# 1. target = 24, cnt = 2, N = 8
# 2. target = 6, cnt = 5, N = 2
# 3. break -> cnt = 6
