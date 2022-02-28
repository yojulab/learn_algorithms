# - 테스트 케이스
# 13  -> 3
# 58  -> 5
# 1   -> 1
# 63  -> 6

# - 프로그래밍 순서
def main():
    # N번 방 번호 받음.
    end_room = int(input())
    # end_room = 13
    # end_room = 58
    # end_room = 1
    # end_room = 63

    # 중앙 1번부터 N번 방까지 가는 최소 방 개수 구함.
    start_room = 1
    minimum_count = 1
    while end_room > start_room:
        start_room = start_room + (6 * minimum_count)
        minimum_count += 1
        pass

    # 최소 방 개수 표시. 
    print(minimum_count)

    pass

if __name__ == '__main__':
    main()