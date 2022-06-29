import sys

N, M = map(int, sys.stdin.readline().split())
A, B, d = map(int, sys.stdin.readline().split())

game_map = []

for _ in range(N) :
    game_map.append(list(map(int, sys.stdin.readline().split())))

# north : 0 / east : 1 / south : 2 / west : 3
directions = [0, 1, 2, 3]
movings = [(-1, 0), (0, 1), (1, 0), (0, -1)]
move_cnt = 0
failure = 0

# A, B = A-1, B-1
game_map[A][B] = -1
while True :
    nd = directions[d-1]
    na = A + movings[nd][0]
    nb = B + movings[nd][1]

    # if new position is in the map
    if na >= 0 and na < N and nb >= 0 and nb < M and game_map[na][nb] == 0 :
        A, B, d = na, nb, nd
        move_cnt += 1
        game_map[na][nb] = -1
        failure = 0
        continue
    else : 
        d = nd
        failure += 1
    
    # backstep or stop
    if failure == 4 :
        failure = 0
        na = A - movings[d][0]
        nb = B - movings[d][1]
        # print(na, nb, game_map[na][nb])

        if not (na >= 0 and na < N and nb >= 0 and nb < M ) :
            break
        elif game_map[na][nb] == 1 :
            break
        elif na >= 0 and na < N and nb >= 0 and nb < M :
            A, B = na, nb
            move_cnt += 1

print(move_cnt)

    



            
