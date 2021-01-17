def binary_search(arr, start, end, target):

    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def shifted_arr_search(shiftArr, target):
    start = 0
    end = len(shiftArr) - 1

    while start <= end:
        mid = (start + end) / 2
        #print("Mid now ", mid)
        elem = shiftArr[mid]

        if elem == target:
            return mid

        if elem > shiftArr[0]:  # First ascending seq
            if target < elem and target >= shiftArr[0]:
                end = mid-1
                # return binary_search(shiftArr, 0 , mid, target)
            else:
                start = mid + 1
        else:  # Second ascending seq
            if target > elem and target <= shiftArr[-1]:
                start = mid + 1
                # return binary_search(shiftArr, mid , len(shiftArr)-1, target)
            else:
                end = mid - 1

        #print("finishing while with", start, end)

    return -1

if __name__ == "__main__":
    ex1 = [1, 2, 3]
    print(shifted_arr_search(ex1, 3))
    print(shifted_arr_search(ex1, 7))
    print(shifted_arr_search(ex1, 50))

    input_ex = [9, 12, 17, 2, 4, 5]
    print(shifted_arr_search(input_ex, 2))
    print(shifted_arr_search(input_ex, 17))
    print(shifted_arr_search(input_ex, 2))
