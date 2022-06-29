################################################
# insertion sort
# 1. at first, start with the second value (assume that first data is sorted)
# 2. otherwise, choose the first element among the un-sorted data
# 3. compare the chosen data and the sorted data element-wise
#   - if the chosen data is smaller than the comparison target, stop
# 4. repeat 2 and 3
# ----------------------------------------------------------
# O(N^2)
# very fast when the data is almost sorted
################################################

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    # decrease j from i to 0
    for j in range(i, 0, -1) :
        # move left one by one
        if array[j] < array[j-1] :
            # swap
            array[j], array[j-1] = array[j-1], array[j]
        # stop if the chosen data is smaller than the comparison target
        else :
            break

print(array)