import java.io.*;
import java.util.*;

class Main {  

  static ArrayList<Integer>[] A;
  static boolean[] visited;
  static int[] D;
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);
    
    int N = sc.nextInt(); // 도시 수
    int M = sc.nextInt(); // 도로 수
    int K = sc.nextInt(); // 최단거리 K
    int X = sc.nextInt(); // 출발도시 번호

    // 초기화
    A = new ArrayList[N + 1];
    for (int i = 1; i <= N; i++) {
      A[i] = new ArrayList<Integer>();
    }
    visited = new boolean[N + 1];
    D = new int[N + 1];

    for (int i = 0; i < M; i++) {
      int s = sc.nextInt();
      int e = sc.nextInt();
      A[s].add(e);
    }

    D[X] = 0;
    BFS(X);

    boolean check = false;
    for (int i = 1; i <= N; i++) {
      if (D[i] == K) {
        check = true;
        System.out.print(i + " ");
      }
    }
    
    if (!check) {
      System.out.print("-1");
    }
    
  }

  public static void BFS(int node) {
    Queue<Integer> q = new LinkedList<>();
    q.add(node);
    visited[node] = true;

    while(!q.isEmpty()) {
      int now = q.remove();
      for (int i : A[now]) {
        if (!visited[i]) {
          visited[i] = true;
          D[i] = D[now] + 1;
          q.add(i);
        }
      }
    }
  }
}