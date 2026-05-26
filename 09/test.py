import queue
import copy

class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include


def kp_BFS():
    global maxProfit
    global bestset

    q = queue.Queue()

    temp = [0] * n
    v = Node(-1, 0, 0, temp)

    # 초기 bound 계산
    initial_bound = compBound(v)

    q.put(v)

    step = 1

    while not q.empty():

        print("\n==============================")
        print(f"[Step {step}]")

        v = q.get()

        print("현재 노드")
        print(f"level={v.level}, weight={v.weight}, profit={v.profit}")
        print(f"include={v.include}")

        # 초기 노드일 때 bound 출력
        if v.level == -1:
            print(f"initial bound={initial_bound}")

        level = v.level + 1

        # 마지막 레벨 도달
        if level >= n:
            print("마지막 레벨 도달")
            step += 1
            continue

        # -------------------------------
        # 물건 포함하는 경우
        # -------------------------------

        weight = v.weight + w[level]
        profit = v.profit + p[level]

        include = v.include[:]

        u = Node(level, weight, profit, include)
        u.include[level] = 1

        print("\n[포함하는 경우]")
        print(f"{level+1}번 물건 포함")
        print(f"weight={u.weight}, profit={u.profit}")
        print(f"include={u.include}")

        # maxProfit 갱신
        if u.weight <= W and u.profit > maxProfit:
            maxProfit = u.profit
            bestset = u.include[:]

            print(">>> maxProfit 갱신!")
            print(f"maxProfit={maxProfit}")

        bound = compBound(u)

        print(f"bound={bound}")

        if bound > maxProfit:
            print("유망 노드 -> 큐 삽입")
            q.put(u)
        else:
            print("가지치기")

        # -------------------------------
        # 물건 포함하지 않는 경우
        # -------------------------------

        u = Node(level, v.weight, v.profit, v.include[:])

        print("\n[포함하지 않는 경우]")
        print(f"{level+1}번 물건 미포함")
        print(f"weight={u.weight}, profit={u.profit}")
        print(f"include={u.include}")

        bound = compBound(u)

        print(f"bound={bound}")

        if bound > maxProfit:
            print("유망 노드 -> 큐 삽입")
            q.put(u)
        else:
            print("가지치기")

        step += 1


def compBound(u):

    if u.weight >= W:
        return 0

    j = u.level + 1
    bound = u.profit
    totweight = u.weight

    # 가능한 만큼 물건 통째로 추가
    while j < n and totweight + w[j] <= W:
        totweight += w[j]
        bound += p[j]
        j += 1

    # 남는 공간 fractional 추가
    if j < n:
        bound += (W - totweight) * p[j] / w[j]

    return bound


# -------------------------------
# 입력 데이터
# -------------------------------

n = 5
W = 13

p = [20, 30, 35, 12, 3]
w = [2, 5, 7, 3, 1]

maxProfit = 0
bestset = [0] * n

# 실행
kp_BFS()

# 결과 출력
print("\n==============================")
print("최종 결과")
print("bestset =", bestset)
print("maxProfit =", maxProfit)