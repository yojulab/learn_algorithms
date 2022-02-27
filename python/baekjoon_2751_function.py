# git :
def merge_sort(array):
    if len(array)<=1: 
        return array 
    mid = len(array)//2 
    #left는 array리스트의 인덱스 0부터 mid전까지 
    left = merge_sort(array[:mid]) 
    #right은 array리스트의 인덱스 mid부터 끝까지 
    right = merge_sort(array[mid:]) 
    i, j, k = 0, 0, 0 
    arr = [] 
    #둘중 하나조건에 부합하지 않을경우 while문 빠져나감 
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            arr.append(left[i]) 
            i+=1 
        else: 
            arr.append(right[j]) 
            j+=1 
    #while문 빠져 나온 후, left혹은 right에 남은 요소들 arr에 넣어주기 
    arr += left[i:] 
    arr += right[j:] 
    return arr

import sys
def main():
    array = []

    # n = int(sys.stdin.readline())
    # for _ in range(n):
    #     array.append(int(sys.stdin.readline()))

    n = 5
    array = [5 ,2 ,3 ,4 ,1]    # 1 ,2 ,3 ,4 ,5
    n = 4   
    array = [22 ,44 ,31 ,17]   # 17 ,22 ,31 ,44 

    array = merge_sort(array)

    for data in array:
        print(data)
        pass

if __name__ == '__main__':
    main()
