def search(l, target, low, high):
    if high >= low:
        mid = (low + high) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            return search(l, target, low, mid-1)
        else:
            return search(l, target, mid+1, high)
    else:
        return -1


l = [1,3,6,8,9,10]

print(search(l, 5, 0, len(l)-1))