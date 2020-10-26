def question3(arr):
    profit = 0
    min_local = arr[0]
    for item in arr:
        profit = max(profit, item - min_local)
        min_local = min(min_local, item)
    return profit

if __name__ == '__main__':
    print("Array: %s resultado %d" % (str([7,1,5,3,6,4]), question3([7,1,5,3,6,4])))
    print("Array: %s resultado %d" % (str([7,6,4,3,1]), question3([7,6,4,3,1])))
    print("Array: %s resultado %d" % (str([1,2,3,4,5]), question3([1,2,3,4,5])))
