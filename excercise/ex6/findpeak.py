def find_peak(hill):
    """
    Assumption: 'hill' is a nonempty list of integers with the guarantee that
    there is some index 0 <= i < len(l) such that the sublist
    hill[0:i+1] is strictly increasing and the sublist hill[i:len(l)] is
    strictly decreasing. So hill[i] is the 'peak' of the hill.

    Return the index i of this peak. Your algorithm should run in O(log n) time.

    You can assume that we will only test your implementation with
    lists that satisfy the above property.

    Examples:
    find_peak([1, 3, 6, 7, 4, 1])
    3

    find_peak([4])
    0

    find_peak([1, 2, 3])
    2

    find_peak([9, 4])
    0

    find_peak([1, 8, 6, 2])
    1
    """
    #case that only contain 1 item
    if len(hill) == 1:
        return 0
    #case that only contain 2 items
    elif len(hill) == 2:
        # print("here")
        if hill[0] < hill[1]:
            return 1
        elif hill[0] >= hill[1]:
            return 0
    #initialzing the variables
    start = 0
    end = len(hill)-1
    while int(end-start) >= 1:
        mid = int((start+end)/2)
        #if the mid point is exactly the peak
        if hill[mid]>hill[mid-1] and hill[mid]>hill[mid+1]:
            return mid
        #if the mid point is inside the progress of decreasing
        elif hill[mid]<hill[mid-1] and hill[mid]>hill[mid+1]:
            end = mid
        #if the mid point is inside the progress of increasing
        elif hill[mid]>hill[mid-1] and hill[mid]<hill[mid+1]:
            start = mid
        if int(end-start) == 1:
            if hill[start]>hill[end]:
                #debug
                #print("herereerererere")
                return start
            else:
                #debug
                #print('wewewewewewewe')
                return end
        #debug
        # print(end,start,mid)
        # print("------------------")
    return mid

# test the function
# print(find_peak([1, 3, 6, 7, 4, 1]))
# print(find_peak([4]))
# print(find_peak([1, 2, 3]))
# print(find_peak([9, 4]))
# print(find_peak([1, 8, 6, 2]))
