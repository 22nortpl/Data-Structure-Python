배열 : 기본 자료구조 중 하나

리스트 vs 튜플
  리스트 :
    list01 = []     # 빈 리스트
    list02 = [1, 2, 3]     #[1, 2, 3]
    list03 = ['A', 'B', 'C', ]     #맨 마지막 원소에 쉼표를 써도 됨
  리스트 함수를 사용:
    list04 = list()     #빈 리스트
    list05 = list('ABC')     #['A', 'B', 'C']문자열의 각 문자로부터 원소를 생성
    list06 = list([1, 2, 3])     #리스트로부터 원소 생성
    list07 = list((1, 2, 3))     #튜플로부터 원소 생성
    list08 = list({1, 2, 3})     #집합으로부터 원소 생성
  특정 범위 : range를 조합
    list09 = list(range(7))     #[0, 1, 2, 3, 4, 5, 6]
    list10 = list(range(3, 8))     #[3, 4, 5, 6, 7]
    list11 = list(range(3, 13, 2))     #[3, 5, 7, 9, 11]
  원소 없는 리스트 : none
    list12 = [none] * 5     #[none, none, none, none, none]
  
  튜플 : 원소 변경 불가능
    tuple01 = ()
    tuple02 = 1,
    tuple03 = (1,)
    tuple04 = 1, 2, 3
    tuple05 = 1, 2, 3,
    tuple06 = (1, 2, 3)
    tuple07 = (1, 2, 3, )
    tuple08 = 'A', 'B', 'C',
  주의 : 튜플은 대부분 값이 여러 개, 한 개만 있는 튜플은 무조건 쉼표 추가
  문자열 혹은 빈 문자열을 튜플로
    tuple09 = tuple()
    tuple10 = tuple('ABC')
    tuple11 = tuple([1, 2, 3])
    tuple12 = tuple({1, 2, 3})
  범위 사용도 리스트와 동일!

  