def main():
   # 한 줄에 고정비용, 가변비용, 노트북 가격을 받음
   fixed_cost, variable_cost, producted_cost = map(int, input().split())
   # fixed_cost, variable_cost, producted_cost = [1000, 70, 170]
   # fixed_cost, variable_cost, producted_cost = [3, 2, 1]
   # fixed_cost, variable_cost, producted_cost = [2100000000, 9, 10]

   if variable_cost >= producted_cost:   # 분모가 - 되는 값 확인
      producted_number = -1
   else:
      # 손익분기점을 찾음 (고정비용 / (판매비용 - 가변비용)) < 생산대수
      # 주의 : 나누기('/') 연산자 사용 시 백준 제출 오류
      producted_number = (fixed_cost // (producted_cost - variable_cost))
      # 수입이 비용보다 많게 하기 위해 생산 대수에 +1
      producted_number += 1

   # 손익분기점 값을 표시
   print(producted_number)
   pass

if __name__ == '__main__':
    main()
