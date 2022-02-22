# - 테스트 케이스
# 1   -> 1/1
# 2   -> 1/2
# 3   -> 2/1
# 4   -> 3/1
# 5   -> 2/2
# 6   -> 1/3
# 7   -> 1/4
# 8   -> 2/3
# 9   -> 3/2
# 14  -> 2/4

# - 프로그래밍 순서
def main():
    # 몇 번째 구할지 받음.
    number = int(input())
    # number = 1
    # number = 3
    # number = 7
    # number = 14
    # number = 50

    # 좌상단 1/1 시작으로 분자(열) 구함.
    # 좌상단 1/1 시작으로 분모(행) 구함.
    col = number
    row = 1
    while col > row:
        col -= row
        row += 1

    if row % 2 == 0:
        numerator = col
        denominator = row-col+1
    else:
        numerator = row-col+1
        denominator = col

    # 분모와 분자를 알맞게 표시.
    print(numerator, denominator, sep='/')

    pass

if __name__ == '__main__':
    main()