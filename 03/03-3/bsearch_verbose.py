from typing import Any, Sequence
def bin_search(a : Sequence, key : Any) -> int:

  pl = 0
  pr = len(a) - 1

  print('   |', end="")
  for i in range(len(a)):
    print(f'{i : 4}', end='')
  print()
  print('---+' + (4 * len(a) + 2) * '-')