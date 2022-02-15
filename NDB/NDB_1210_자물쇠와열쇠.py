# Hint : 자물쇠 크기 3배

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
  n = len(a) # 행
  m = len(a[0]) # 열
  result = [[0] * n for _ in range(m)] # 결과 리스트

  for i in range(n):
    for j in range(m):
      # 90도 회전하여 저장
      result[j][n - i - 1] = a[i][j]
  
  return result

# 자물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
  lock_length = len(new_lock) // 3
  # 새로 만든 lock의 1/3지점부터 2/3지점까지 확인
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  # n : 자물쇠
  n = len(lock)
  # m : 열쇠
  m = len(key)
  # 새로운 자물쇠 생성 (3배)
  new_lock = [[0] * (n * 3) for _ in range(n * 3)]
  # 새로운 자물쇠 중앙에 기존 좌물쇠 삽입
  for i in range(n):
    for j in range(n):
      new_lock[i + n][j + n] = lock[i][j]

  # 4가지 방향에 대해 완전탐색
  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
    # 큰 자물쇠의 2/3 지점까지(=중간 지점) 탐색
    for x in range(n * 2):
      for y in range(n * 2):
        # 3배 큰 자물쇠 중간에 열쇠 맞추기
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] += key[i][j]
        # 큰 자물쇠에 열쇠가 정확히 들어맞는지 check
        if check(new_lock) == True:
          return True
        # 큰 자물쇠에서 열쇠 고대로 다시 빼기(backtrack)
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] -= key[i][j]
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]] # m
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]] # n

print(solution(key, lock))
