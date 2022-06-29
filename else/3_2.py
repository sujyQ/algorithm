import sys

N, M, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort(reverse=True)

repeat = int(M/(K+1)) * K + int(M%(K+1))

ans = num_list[0]*repeat + num_list[1]*(M-repeat)

print(ans)