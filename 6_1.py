################################################
# selection sort
# 1. select the smallest value among the un-sorted data
# 2. swap selected one with the front value of the un-sorted data
# 3. repeat 1 and 2 till just one data left
# ----------------------------------------------------------
# O(N^2)
#################################################

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :
    min_index = i
    # get index of minimum data
    for j in range(i+1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j

    # swap
    array[i], array[min_index] = array[min_index], array[i]

print(array)