def main():
    # 배달 총 킬로그래 받기(3 ≤ N ≤ 5000)
    n_weight = int(input())
    # n_weight = 18  # 4
    # n_weight = 4   # -1
    # n_weight = 6   # 2
    # n_weight = 9   # 3
    # n_weight = 11  # 3
    # 배달 최소 봉지 개수 구하기.
    minimum_bag = 0

    while n_weight >= 0:
        if n_weight % 5 == 0:
            minimum_bag += int(n_weight // 5)
            print(minimum_bag)
            break

        n_weight -= 3
        minimum_bag += 1

    # 배달 최소 봉지 개수 표시(정확하게 N킬로그램을 만들 수 없다면 -1을 출력)
    else:
        print(-1)    
    pass

if __name__ == '__main__':
    main()