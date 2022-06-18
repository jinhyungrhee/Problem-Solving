import java.io.*;
import java.util.*;

class Main {  
  static ArrayList<Integer>[] A;
  static boolean[] visited;
  static int[] T; // 신뢰도 배열
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt(); // 노드수
    int M = sc.nextInt(); // 에지수

    // 초기화
    A = new ArrayList[N + 1];
    for (int i = 1; i <= N; i++) {
      A[i] = new ArrayList<Integer>();
    }
    // visited = new boolean[N + 1];
    T = new int[N + 1];

    // 입력값 저장
    for (int i = 0; i < M; i++) {
      int curr = sc.nextInt();
      int target = sc.nextInt();
      
      A[curr].add(target);
    }

    // 모든 노드에서 각각 BFS 실행 ***
    for (int i = 1; i <= N; i++) {
      visited = new boolean[N + 1]; // 할때마다 visited배열 초기화
      BFS(i); // 매번 BFS할 때마다 신뢰도 배열(T) 갱신
    }
    // BFS(1); // X

    int MAX = 0;
    for (int i = 1; i <= N; i++) {
      if (T[i] > MAX) {
        MAX = T[i];
      }
    }

    for (int i = 1; i <= N; i++) {
      if (T[i] == MAX)
        System.out.print(i + " ");
    }
    
    
  }
  public static void BFS(int node) {
    Queue<Integer> q = new LinkedList<>();
    q.add(node);
    visited[node] = true;

    while(!q.isEmpty()) {
      int now = q.remove();
      for(int i : A[now]) {
        if (!visited[i]) {
          T[i]++;
          q.add(i);
          visited[i] = true;
        }
      }
    }
  }

}