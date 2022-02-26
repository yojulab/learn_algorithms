# git : 
def main():
    # 정렬할 수 개수 받음. N(1 ≤ N ≤ 1,000)
    sort_count = int(input())
    # N개 수를 줄 단위로 받음.(정수, 수는 중복 없음.)
    sort_numbers = list()
    for _ in range(sort_count):
        sort_numbers.append(int(input()))
    # sort_count = 5
    # sort_numbers = [5 ,2 ,3 ,4 ,1]    # 1 ,2 ,3 ,4 ,5
    # sort_count = 4   
    # sort_numbers = [22 ,44 ,31 ,17]   # 17 ,22 ,31 ,44 

    # 받은 수를 오름차순으로 정렬.
    for index in range(sort_count): 
        min_index = index # 가장 작은 원소의 인덱스 
        for idx in range(index+1, sort_count): 
            if sort_numbers[min_index] > sort_numbers[idx]: 
                min_index = idx 
        sort_numbers[index], sort_numbers[min_index] = sort_numbers[min_index], sort_numbers[index] # swap

    # 정렬한 수를 줄 단위로 표시.
    for index in range(sort_count):
        print(sort_numbers[index])

    pass

if __name__ == '__main__':
    main()