# a부터 b까지의 정수 합 구하기 1

print("a부터 b까지의 정수의 합을 구합니다.")
a = int(input("a값을 입력하세요 : "))
b = int(input("b값을 입력하세요 : "))

if a > b:
  a, b = b, a
  
sum = 0
for i in range(a, b+1):
  if i < b:
    print(f'{i} + ', end='')
  else:
    print(f'{i} = ', end='')
  sum += i

print(sum)