cur_pos = str(input())


##### my answer
cur_y = cur_pos[1]

x_position = ['a', 'b', 'c', 'd', 'e', 'f', 'g',' h']

cur_x = x_position.index(cur_pos[0])+1
cur_y = int(cur_pos[1])

cnt = 0

for i in range(1, 9) :
    for j in range(1, 9) :
        if cur_x != i and cur_y != j :
            if abs(cur_x - i) + abs(cur_y - j) == 3 :
                print(i, j)
                cnt += 1

print(cnt)


##### answer in book

# get current posiion
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# possible moving directions
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# check if moving is available

result = 0
for step in steps :
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result +=1

print(result)