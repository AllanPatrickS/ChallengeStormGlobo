def question1(arr, target):
    aux = arr.copy()
    aux.sort()
    start = 0
    end = len(arr) - 1
    while (start != end):
        if (aux[start] + aux[end] > target):
            end -= 1
        elif (aux[start] + aux[end] < target):
            start += 1
        else:
            return [arr.index(aux[start]), arr.index(aux[end])]


if __name__ == '__main__':
    print("Array: %s Alvo: %d indices %s" % (str([2, 7, 11, 15]), 9, question1([2, 7, 11, 15], 9)))
    print("Array: %s Alvo: %d indices %s" % (str([2, 11, 7, 15]), 9, question1([2, 11, 7, 15], 9)))
    print("Array: %s Alvo: %d indices %s" % (str([7, 11, 15, 2]), 9, question1([7, 11, 15, 2], 9)))