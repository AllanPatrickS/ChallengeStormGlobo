def question1(arr, target):
    for item in arr:
        if -1 < (target - item) and arr.index(target - item):
            return [arr.index(item), arr.index(target - item)] 

if __name__ == '__main__':
    print("Array: %s Alvo: %d indices %s" % (str([2, 7, 11, 15]), 9, question1([2, 7, 11, 15], 9)))
    print("Array: %s Alvo: %d indices %s" % (str([2, 11, 7, 15]), 9, question1([2, 11, 7, 15], 9)))
    print("Array: %s Alvo: %d indices %s" % (str([7, 11, 15, 2]), 9, question1([7, 11, 15, 2], 9)))