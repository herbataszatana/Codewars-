def find_smallest_int(arr):
    # Code here
    min = arr[0];  
    for i in range(0, len(arr)):    
    #Compare elements of array with min    
       if(arr[i] < min):    
           min = arr[i];    
    print(min)

arr=[1,5,2, 0]

find_smallest_int(arr)