import java.io.*;
import java.util.*;

class Main {  
  // 전역변수 정의
  static int[] dx = {0, 1, 0, -1};
  static int[] dy = {1, 0, -1, 0};
  static boolean[][] visited;
  static int[][] A;
  static int N, M;
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    A = new int[N][M];
    visited = new boolean[N][M];

    for (int i = 0 ; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      String line = st.nextToken(); // String으로 type casting?
      for (int j = 0; j < M; j++) {
        // substring() 사용해서 한 글자씩 잘라서 대입
        A[i][j] = Integer.parseInt(line.substring(j, j + 1));
      }
    }
    // BFS 실행
    BFS(0, 0);
    // 가장 마지막 위치의 최단거리 출력
    System.out.println(A[N - 1][M - 1]);
  }

  public static void BFS(int i, int j) {
    Queue<int[]> q = new LinkedList<>();
    // 큐에 시작 노드 삽입 **
    q.add(new int[] {i , j});
    visited[i][j] = true;

    while(!q.isEmpty()) {
      int[] now = q.poll();
      // visited[i][j] = true;
      for (int k = 0; k < 4; k++) {
        int nx = now[0] + dx[k];
        int ny = now[1] + dy[k];
        if (nx >= 0 && ny >= 0 && nx < N && ny < M) { // 좌표 유효성 검사
          if (A[nx][ny] != 0 && !visited[nx][ny]) {
            visited[nx][ny] = true;
            // 깊이(depth) 업데이트 하기 ***
            A[nx][ny] = A[now[0]][now[1]] + 1; // 기존 값에서 +1
            q.add(new int[] {nx, ny});
          }
        }
      }
      
    }
    
  }
}
