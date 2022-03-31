# 위상정렬 - 팀 간의 순위를 그래프로 표현(자기보다 낮은 등수의 팀을 가리키도록 함)
from collections import deque

for _ in range(int(input())):
  n = int(input()) # 팀 수
  # 모든 노드에 대한 진입차수
  indegree = [0] * (n + 1)
  # 각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화
  graph = [[False] * (n + 1) for i in range(n + 1)]
  # 작년 순위 정보
  data = list(map(int, input().split()))# [5, 4, 3, 2, 1]
  # 방향 그래프 간선 정보 초기화
  for i in range(n):
    for j in range(i+1, n):
      graph[data[i]][data[j]] = True
      indegree[data[j]] += 1 #[0, 1, 2, 3, 4]

  # 올해 변경된 순위 정보 입력
  m = int(input())
  for i in range(m):
    a, b = map(int, input().split())
    # 간선 방향 뒤집기
    if graph[a][b]: # 변경된 경우
      graph[a][b] = False
      graph[b][a] = True
      indegree[a] += 1 # a가 더 낮아지고
      indegree[b] -= 1 # b가 더 높아짐
    else:
      graph[a][b] = True
      graph[b][a] = False
      indegree[a] -= 1
      indegree[b] += 1

  # 위상정렬 시작
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q = deque()

  # 처음 시작 시 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)

  certain = True # 위상 정렬 결과가 오직 하나인지 여부 체크
  cycle = False # 그래프 내 사이클이 존재하는지 여부 체크

  # 노드 개수만큼 반복
  for i in range(n):
    # 큐가 비어있으면 사이클 발생
    if len(q) == 0:
      cycle = True
      break
    # 큐의 원소가 2개 이상이면, 가능한 정렬 결과가 여러 개임
    if len(q) >= 2:
      certain = False
      break
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for j in range(1, n+1):
      if graph[now][j]:
        indegree[j] -= 1
        # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
        if indegree[j] == 0:
          q.append(j)

  # 사이클이 발생하는 경우(일관성이 없는 경우)
  if cycle:
    print("IMPOSSIBLE")
  # 위상 정렬 결과가 여러 개인 경우
  elif not certain:
    print("?")
  # 위상 정렬을 수행한 결과 출력
  else:
    for i in result:
      print(i, end=' ')
    print()