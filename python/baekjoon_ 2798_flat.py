# git : https://github.com/SanghunOh/with_algorithm
def main():
    # 카드 장수와 3장을 합한 최대수 받기
    card_count, maximum = map(int, input().split())
    card_number_list = list(map(int, input().split()))
    # card_count, maximum = 5, 21    
    # card_number_list = [5, 6, 7, 8, 9]  # 21
    # card_count, maximum = 10, 500
    # card_number_list = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]    # 497

    # 카드 조합 통한 최대수 보다 작은 합산 찾기
    card_number_length = len(card_number_list)
    near_number = 0
    for first in range(0, card_number_length-2):
        for second in range(first+1, card_number_length-1):
            for third in range(second+1, card_number_length):
                if(card_number_list[first] + card_number_list[second] + card_number_list[third] > maximum):
                    continue
                else:
                    near_number = max(near_number ,card_number_list[first] + card_number_list[second] + card_number_list[third])

    # 찾은 최대수와 가까운 수 표시
    print(near_number)    

    pass

if __name__ == '__main__':
    main()