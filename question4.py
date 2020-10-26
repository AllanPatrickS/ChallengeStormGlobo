def question4(arr):
    result = 0
    left = 0
    right = 0
    start = 0
    end = len(arr)-1
    while(start <= end):  
        if(arr[start] < arr[end]): 
            if (arr[start] < left): 
                result += left - arr[start]
            elif (arr[start] > left): 
                left = arr[start] 
            start += 1
        else: 
            if (arr[end] < right): 
                result += right - arr[end]
            elif (arr[end] > right): 
                right = arr[end]
            end-= 1
    return result

if __name__ == '__main__':
    print("Array: %s resultado %d" % (str([0,1,0,2,1,0,1,3,2,1,2,1]), question4([0,1,0,2,1,0,1,3,2,1,2,1])))
    print("Array: %s resultado %d" % (str([4,1,0,2,1,0,1,3,2,1,2,5]), question4([4,1,0,2,1,0,1,3,2,1,2,5])))
