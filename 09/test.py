#n‐Queens 문제해결 알고리즘
def promising(i,col):
  k = 0
  switch = True
  while(k<i and switch == True):
  #k가 i보다 작고,아직 유망하다면(switch가 True라면)
    if(col[i] == col[k] or abs(col[i]-col[k]) ==(i-k)):
    #col[i]를 col[0]부터 col[i‐1]까지 비교‐같은 행
      switch = False #그럼 switch를 False로
    k += 1 # k 를 1증가
  return switch

def queens(n,i,col):
  if promising(i,col):
    # 만약 i번째 depth column 에서유망하면
    if i == n-1: #끝까지(여기서는index6까지)말을놨다면
      print(col) #column을출력한다
    else: # 아직 말을 놓지않은 column이 존재하면
      for k in range(n):
        col[i+1] = k
        #다음 column의 모든 칸에 말을 놓은 후에
        queens(n, i+1, col) # 다시 queens를 돌린다
n = int(input("원하는 여왕말 수를 입력하세요. : "))
col=n*[0]
#col[i]는i번째queen이위치한column값
queens(n,-1,col)