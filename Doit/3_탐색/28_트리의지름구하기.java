import java.io.*;
import java.util.*;

class Main {  
  // 전역변수 정의
  static ArrayList<Edge>[] A;
  static boolean[] visited;
  static int[] distance; // 거리 저장 배열
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    
    // 이차원 인접 리스트 생성 및 초기화
    A = new ArrayList[N + 1];
    for (int i = 1; i <= N; i++) {
      A[i] = new ArrayList<Edge>();
    }

    for (int i = 0; i < N; i++) {
      int node = sc.nextInt();
      // -1이 입력될 때까지 반복
      while(true) {
        int e = sc.nextInt();
        // int value = sc.nextInt(); // Q1. value 입력이 여기에 있으면 에러나는 이유? **
        if (e == -1) {
          break;
        }
        int value = sc.nextInt();
        A[node].add(new Edge(e, value));
      }
    }

    // 방문 리스트 생성 및 초기화 (자동 전부 false)
    visited = new boolean[N + 1];
    // 거리 저장 배열 생성 및 초기화 (자동 전부 0)
    distance = new int[N + 1];

    // 임의의 점을 시작점으로 BFS 실행 <첫 번째 BFS>
    BFS(1);
    // BFS 한 번 실행 후, 변경된 distance 배열에서 가장 큰 값을 갖는 노드를 다음 시작점으로 지정
    // Q2. 모든 경우에 대해서 항상 두 번의 BFS만으로 동일한 결과를 보장할 수 있는가? **
    int MAX = 1;
    for (int i = 2; i <= N; i++) {
      if (distance[i] > distance[MAX]) {
        MAX = i;
      }
    }

    // 방문 리스트, 거리 저장 배열 다시 초기화
    visited = new boolean[N + 1];
    distance = new int[N + 1];

    // 임의의 노드로부터 가장 먼 노드를 기준으로 다시 BFS 수행 <두 번째 BFS>
    BFS(MAX);

    // 새로 구해진 거리 배열을 오름차순 정렬 후 가장 큰 값(=마지막 값) 출력
    Arrays.sort(distance);
    System.out.println(distance[N]);
    
  }

  static void BFS(int index) {
    Queue<Integer> q = new LinkedList<>();
    q.add(index);
    visited[index] = true;

    while(!q.isEmpty()) {
      int now = q.poll();
      // 연결노드 중 방문하지 않은 노드 탐색
      for (Edge i : A[now]) {
        int e = i.e;
        int v = i.value;
        if (!visited[e]) {
          q.add(e);
          visited[e] = true;
          distance[e] = distance[now] + v;
        }
      }
    }
  }

}

class Edge {
  int e; // 목적지 노드
  int value; // 에지의 가중치

  public Edge(int e, int value) {
    this.e = e;
    this.value = value;
  }
  
}
