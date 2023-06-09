# --------------------------------------------- #
# 구역의 수
N = int(input())

# 연결 상태를 표시할 그래프
graph = [[] for _ in range(N + 1)]

# 탐색 기록을 저장하기 위한 공간 정의
visited = [0 for _ in range(N + 1)]
visited = [0] * (N + 1)

# 인구 수
population = [0] + list(map(int, input().split()))

# 연결 정보
for i in range(1, N + 1):
    j = list(map(int, input().split()))
    graph[i] = j[1:]

# 전체 인구 수
total = sum(population)

# 두 지역 간 인구 수 차이를 바인딩 할 변수
answer = total
# --------------------------------------------- #

# 입력된 sector에서 연결이 1개 인지 검증
def chk_sector(sector : list):
    for i in range(1, N + 1):
        if sector[i] == 0: # sector 요소가 0인 곳 탐지
            start = i
            break
    stack = [start]
    # dfs 탐색을 위한 stack 생성

    while stack: # sector에서 start node와 연결된 node는 모두 1로 표시
        u = stack.pop() # stack의 마지막 요소부터 탐색

        # sector 안의 u node를 1로 표시
        if sector[u]:
            continue
        sector[u] = 1

        for v in graph[u]: # graph[u] 에 있는 node를 stack에 넣는다.
            stack.append(v) # 다음 번 탐색에서 v를 탐색한다.
    
    for i in sector[1:]:
        if i == 0:
            # sector 안에 0으로 표시된 node 가 있다는 것은
            # 모든 node가 연결되지 않았다는 뜻이다.
            return False 
    return True


# sector를 2개로 나누는 함수
def divide_sector(sector : list): # 전체 node에 대해 0과 1로 구분 된 리스트 입력
    sector1 = sector[:] # sector1은 이미 방문한 곳
    sector2 = [int(not i) for i in sector1] # sector2는 아직 방문하지 않은 곳
    if not chk_sector(sector1):
        return False # sector1이 모두 연결되지 않았으므로 False
    if not chk_sector(sector2):
        return False # sector2이 모두 연결되지 않았으므로 False
    return True


def sum_population(idx, people):
    global answer

    if people > total // 2: # 더한 인구의 수가 전체 절반 이상이면 종료
        return
    
    if idx == N + 1: # 모든 지역 탐색을 했을 때
        diff = abs(total - people * 2) # 두 지역 간 차이 계산
        if diff < answer and divide_sector(visited): # 차이가 전체 인구보다 작고, 지역이 잘 나눠져 있으면
            answer = diff # 답을 update
        return

    visited[idx] = 1
    sum_population(idx + 1, people + population[idx])
    visited[idx] = 0
    sum_population(idx + 1, people)

    return

# --------------------------------------------- #
sum_population(1, 0)

if answer == total:
    print(-1)
else:
    print(answer)
# --------------------------------------------- #