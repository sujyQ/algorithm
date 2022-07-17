from collections import deque

def solution(maps):
    if maps[-2][-2] == 0 and maps[-2][-1] == 0 and maps[-1][-2] == 0 :
        return -1
    
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    
    def DFS(cur_x, cur_y, count, count_list) :

        if cur_x == len(maps[0])-1 and cur_y == len(maps)-1 :
            count_list.append(count)
        
        else :
            for _x, _y in zip(x, y) :
                # print(_x, _y)
                move_x, move_y = cur_x + _x, cur_y + _y
                if move_x < len(maps) and move_x >= 0 and move_y < len(maps[0]) and move_y >= 0 and maps[move_y][move_x] == 1 :
                    # stack.append([move_x, move_y])
                    # print(move_x, move_y)
                    maps[move_y][move_x] = 0
                    DFS(move_x, move_y, count+1, count_list)
        return count_list
    
    return min(DFS(0, 0, 0, []))+1
    