from max import max_of

print("배열의 최댓값을 구합니다.")
print('주의 : "End"를 입력하면 종료합니다.')

number = 0    #원소의 개수
x = []

while True:
  s = input(f'x[{number}]값을 입력하세요.')
  if s == 'End' or s == 'end':
    break
  x.append(int(s))
  number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')     #참고로 max.py에서 if문 이전의 내용이 적용됨.