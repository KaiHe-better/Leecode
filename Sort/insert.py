
def dichotomy_sorted_insert(sorted_array):
    insert_num = 4
    
    low_index = 0
    high_index = len(sorted_array)
    while low_index < high_index :
        insert_index = int((low_index+high_index) /2)
        if sorted_array[insert_index] < insert_num:
            low_index +=1
        elif sorted_array[insert_index] > insert_num:
            high_index -=1
        else:
            break
    
    sorted_array.insert(high_index, insert_num)
    return sorted_array


# 一个有序数组中，寻找小于等于某个数最左侧的数的index
def dichotomy_sorted_find(sorted_array):
    find_num = 6
    low_index = 0
    high_index = len(sorted_array)
   
    # while len(sorted_array[low_index:high_index])>1 :
    while low_index<high_index-1 :
        middle_index = int((low_index+high_index)/2)
        if sorted_array[middle_index]<find_num:
            low_index = middle_index
        else:
            high_index = middle_index
    
    return low_index, sorted_array[:low_index]
                

def recursive_max(unsorted_array, L, R):
    if L==R-1:
        return unsorted_array[L]
    
    middle = int((R+L)/2)
    left_max = recursive_max(unsorted_array, 0, middle)
    right_max = recursive_max(unsorted_array, middle, R)
    return max(left_max, right_max)


# print(dichotomy_sorted_insert(sorted_array))
# print(dichotomy_sorted_find(sorted_array))
# print(recursive_max(unsorted_array, 0, len(unsorted_array) ) )