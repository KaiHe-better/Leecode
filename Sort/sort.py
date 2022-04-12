unsorted_array_small  = [1,3,4,2,5]
unsorted_array_small_1  = [3,2,4,5,0]
# unsorted_array  =   [3, 1, 1, 2, 2, 6, 9, 4, 4, 3, 9, 10]
unsorted_array  =   [32, 1, 31, 22, 2, 46, 9, 54, 74, 83, 9, 10]
sorted_array  = [1, 1, 2, 2, 3, 3, 3, 5, 5, 6, 6, 7, 7, 8, 8, 8, 8, 8, 9]


def bubble_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        for j in range(len(unsorted_array)-i-1):
            if unsorted_array[j]>unsorted_array[j+1]:
                unsorted_array[j], unsorted_array[j+1] = unsorted_array[j+1], unsorted_array[j]
    return unsorted_array


def choose_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        max_index = 0
        for j in range(len(unsorted_array)-i):
            if unsorted_array[max_index]<unsorted_array[j]:
                max_index = j
        unsorted_array[max_index], unsorted_array[j] = unsorted_array[j], unsorted_array[max_index]
    return unsorted_array


def insert_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        for j in range(i, 0, -1):
            if unsorted_array[j] < unsorted_array[j-1]:
                unsorted_array[j], unsorted_array[j-1] = unsorted_array[j-1], unsorted_array[j]
            else:
                break
    return unsorted_array


def merge_sort(unsorted_array, L_index, R_index):
    
    def merge(unsorted_array, L_index, R_index, mid_index):
        help_array = [0]*(R_index-L_index+1)
        P1 = L_index
        P2 = mid_index+1
        new_index = 0
        
        while (P1<=mid_index) and (P2<=R_index):
            if unsorted_array[P1]<unsorted_array[P2]:
                help_array[new_index] = unsorted_array[P1]
                P1+=1
                new_index+=1
            else:
                help_array[new_index] = unsorted_array[P2]
                P2+=1
                new_index+=1
                
        while P1<=mid_index:
            help_array[new_index] = unsorted_array[P1]
            P1+=1
            new_index+=1
        
        while P2<=R_index:
            help_array[new_index] = unsorted_array[P2]
            P2+=1
            new_index+=1
        
        for i in range(len(help_array)):
            unsorted_array[L_index+i] =  help_array[i]
            
    def process(unsorted_array, L_index, R_index):
        if L_index < R_index:
            mid_index = L_index + ( (R_index-L_index)>>1 )
            process(unsorted_array, L_index, mid_index)
            process(unsorted_array, mid_index+1, R_index)
            merge(unsorted_array, L_index, R_index, mid_index)
   
    
    if (unsorted_array is None) or (len(unsorted_array)<2):
        return unsorted_array
    else:
        process(unsorted_array, L_index, R_index)
        return unsorted_array

    return unsorted_array


def quick_sort(arr, L, R):
    
    def partitiion(arr, L, R):
        less = L-1
        more = R
        while L<more:
            if arr[L]<arr[R]:
                arr[L], arr[less+1] = arr[less+1], arr[L]
                L+=1
                less+=1
            elif arr[L]>arr[R]:
                arr[L], arr[more-1] = arr[more-1], arr[L]
                more-=1
            else:
                L+=1
        arr[R], arr[more] = arr[more], arr[R]
        
        return less+1, more
    
    def process(arr, L, R):
        if L<R:
            less, more = partitiion(arr, L, R)
            process(arr, L, less-1)
            process(arr, more+1, R)
            
    if (arr is None) or len(arr)<2:
        return arr
    elif (R-L<60):
        return  insert_sort(arr)
    else:
        process(arr, L, R)  
        return arr


def heap_sort(arr):
    
    def heap_insert(arr, index):
        while arr[index]>arr[int((index-1)/2)]:
            arr[index], arr[int((index-1)/2)] = arr[int((index-1)/2)], arr[index]
            index = int((index-1)/2)
          
    def heapify(arr, index, heap_size): 
        left = index *2+1
        while left<heap_size:
            if (left+1<heap_size):
                largest = left+1 if (arr[left] < arr[left+1]) else left
            else:
                largest = left
                
            largest = index if arr[index] > arr[largest] else largest
        
            if largest==index:
                break
            
            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest
            left = index*2+1
        
    
    if (arr is None) or len(arr)<2:
        return arr
    else:
        # for i in range(len(arr)):
        #     heap_insert(arr, i)
        
        for i in range(len(arr)-1, -1 , -1):
            heapify(arr, i, len(arr))
     
        heap_size = len(arr)
        heap_size-=1
        arr[0], arr[heap_size] = arr[heap_size], arr[0]
        while heap_size>0 :
            heapify(arr, 0, heap_size)
            heap_size-=1
            arr[0], arr[heap_size] = arr[heap_size], arr[0]
    
    return arr


def bucket_sort(arr):
    
    def get_digit(num, d):
        num = str(num)[::-1]
        if len(num)>d:
            return int(num[d])
        else:
            return 0
    
    def get_max_digit(arr):
        max_num = max(arr)
        return len(str(max_num))
    
    def radix_sort(arr, L, R, digit):
        radix = 10
        bucket = [""]* len(arr)
        for d in range(0, digit):
            count = [0]*radix
            for i in range(L, R):
                j = get_digit(arr[i], d)
                count[j] += 1
            
            for i in range(1, radix):
                count[i] = count[i]+count[i-1]
                
            for i in range(R-1, L-1, -1):
                j = get_digit(arr[i], d)
                bucket [ count[j]-1 ] = arr[i]
                count[j]-=1
                
            for i in range(L, R):
                arr[i] = bucket[i-L]
    
    max_len = get_max_digit(arr)         
    radix_sort(arr, 0, len(arr), max_len)
    return arr



# print(bubble_sort(unsorted_array))
# print(choose_sort(unsorted_array))
# print(insert_sort(unsorted_array))
# print(merge_sort(unsorted_array, 0, len(unsorted_array)-1 ) )
print(quick_sort(unsorted_array, 0, len(unsorted_array)-1) )
# print(heap_sort(unsorted_array))
# print(bucket_sort(unsorted_array))






def merge_sort_for_small_sum(unsorted_array_small, L, R) :
    
    def merge(array, L, R, mid):
        p1 = L
        p2 = mid+1
        new_index = 0
        temp_array = [""]*(R-L+1)
        temp_small_num = 0
        while p1<=mid and p2<=R:
            if array[p1]<array[p2]:
                temp_small_num = temp_small_num + (R-p2+1) * array[p1]
                temp_array[new_index] = array[p1]
                p1+=1
                new_index+=1
                
            else:
                temp_array[new_index] = array[p2]
                p2+=1
                new_index+=1
                
        while p1<mid:
             temp_array[new_index] = array[p1]
             p1+=1
             new_index+=1
        
        while p2<=R:
             temp_array[new_index] = array[p2]
             p2+=1
             new_index+=1
        
        for i in range(len(temp_array)):
            array[L+i] =  temp_array[i]   
        
        return temp_small_num
  
    def process(unsorted_array_small, L, R):
        mid = L + ((R-L)>>1)
        if L==R:
            return 0
        else:
            return process(unsorted_array_small, L, mid) + \
                process(unsorted_array_small, mid+1, R) + \
                merge(unsorted_array_small, L, R, mid)
    
    if len(unsorted_array)<2 or unsorted_array==None:
        return 0
    else:
        return process(unsorted_array_small, L, R)
    
# still wrong !
def merge_sort_for_reverse_pair(unsorted_array, L_index, R_index):
    
    def merge(unsorted_array, L_index, R_index, mid_index):
        help_array = [0]*(R_index-L_index+1)
        P1 = L_index
        P2 = mid_index+1
        new_index = 0
        pair_num = 0
        pair_list = []
        while (P1<=mid_index) and (P2<=R_index):
            if unsorted_array[P1]<=unsorted_array[P2]:
                help_array[new_index] = unsorted_array[P1]
                P1+=1
                new_index+=1
            else:
                pair_num = pair_num + 1
                pair_list.append((unsorted_array[P1], unsorted_array[P2]))
                
                help_array[new_index] = unsorted_array[P2]
                P2+=1
                new_index+=1
                
                
        while P1<=mid_index:
            help_array[new_index] = unsorted_array[P1]
            P1+=1
            new_index+=1
        
        while P2<=R_index:
            pair_num+=1
            pair_list.append((unsorted_array[P1], unsorted_array[P2]))
            
            help_array[new_index] = unsorted_array[P2]
            P2+=1
            new_index+=1
            
            
        for i in range(len(help_array)):
            unsorted_array[L_index+i] =  help_array[i]
        return pair_num, pair_list
    
    if L_index == R_index:
        return 0, []
    
    mid_index = L_index + ( (R_index-L_index)>>1 )
    pair_num_1, pair_list_1 = merge_sort_for_reverse_pair(unsorted_array, L_index, mid_index)
    pair_num_2, pair_list_2 = merge_sort_for_reverse_pair(unsorted_array, mid_index+1, R_index)
    pair_num_3, pair_list_3 = merge(unsorted_array, L_index, R_index, mid_index)
    
    return (pair_num_1+pair_num_2+pair_num_3), (pair_list_1+pair_list_2+pair_list_3)
    

# given a num, a arr, asking the (left part of arr) <= the number, (right part of arr) > num
def quick_sort_pre_1(arr, num):
    P = -1
    index = 0
    while index<len(arr) and ( (P+1)<len(arr) ):
       if arr[index]<=num:
           arr[index], arr[P+1] = arr[P+1], arr[index]
           P+=1
       index+=1
    return arr

# 荷兰国旗问题
# given a num, a arr, asking the (left part of arr) < the number, (mid of arr) = the number, (right part of arr) > num
def quick_sort_pre_2(arr, num):
    S = -1
    E = len(arr)
    index = 0
    while index<E:
        if arr[index]<num:
            arr[index], arr[S+1] = arr[S+1], arr[index]
            index +=1
            S+=1
        elif arr[index]==num:
            index +=1
        else:
            arr[index], arr[E-1] = arr[E-1], arr[index]
            E-=1
    return arr



# print(merge_sort_for_small_sum(unsorted_array_small, 0, len(unsorted_array_small)-1 ) )
# print(merge_sort_for_reverse_pair(unsorted_array_small_1, 0, len(unsorted_array_small_1)-1 ) )
# print(quick_sort_pre_1(unsorted_array, 3) )
# print(quick_sort_pre_2(unsorted_array, 3) )



