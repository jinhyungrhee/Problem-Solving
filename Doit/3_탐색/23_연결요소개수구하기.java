import java.io.*;
import java.util.*;

class Main {
  // 전역 변수로 정의
  static ArrayList<Integer>[] A;
  static boolean[] visited;

  
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken()); // 노드 수
    int M = Integer.parseInt(st.nextToken()); // 에지 수

    // 전역변수로 정의한 인접리스트와 방문 배열 생성 및 초기화
    A = new ArrayList[N + 1]; // 타입 명시 안 해도 생성 가능**
    visited = new boolean[N + 1];
    for (int i = 1; i <= N; i++) {
      A[i] = new ArrayList<Integer>(); // 이차원 인접리스트 생성
    }

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int s = Integer.parseInt(st.nextToken());
      int e = Integer.parseInt(st.nextToken());
      // 양방향 에지 이차원 인접리스트에 기록
      A[s].add(e);
      A[e].add(s);
    }

    int count = 0;
    for (int i = 1; i <= N; i++) {
      if (!visited[i]) {
        count++;
        DFS(i);
      }
    }
    System.out.println(count);
  }
  // Q.언제는 public 쓰고, 언제는 private 쓰고, 언제는 아예 안붙이는데(=public) 정확한 기준이 뭘까?**
  private static void DFS(int v) {
    if (visited[v]){
      return;
    }
    // 방문한 노드 기록 
    visited[v] = true;
    // 연결 노드 중 방문하지 않았던 노드만 탐색하여 dfs 실행 (재귀호출, for-each 사용) **
    for (int i : A[v]) {
      if (visited[i] == false) {
        DFS(i);
      }
    }
  }
}
