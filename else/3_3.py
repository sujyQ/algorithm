import sys

N, M = map(int, sys.stdin.readline().split())

row_min = []
for _ in range(N) :
    row = list(map(int, sys.stdin.readline().split()))
    row_min.append(min(row))

print(max(row_min))

##################################################
# we don't have to use list 'row_min'
# just compare the lowest one in row and the highest number until now
##################################################

result = 0                              # 1 <= num <= 10000 --> initialize 'result' as 0

for _ in range(N) :
    row = list(map(int, sys.stdin.readline().split()))
    result = max(result, min(row))

print(result)
