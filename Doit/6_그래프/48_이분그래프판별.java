import java.io.*;
import java.util.*;

class Main {  
  static ArrayList<Integer>[] A;
  static boolean[] visited;
  // A,B 집합 구분하기 위한 배열(이분그래프 체크 배열) -> 0과 1로 구분**
  static int[] check;
  // 이분그래프 체크 flag**
  static boolean isEven; 
  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int TC = sc.nextInt();
    for (int i = 0; i < TC; i++) {
      int N = sc.nextInt();
      int E = sc.nextInt();

      // 초기화
      A = new ArrayList[N + 1];
      for (int j = 1; j <= N; j++) {
        A[j] = new ArrayList<Integer>();
      }
      visited = new boolean[N + 1];
      check = new int[N + 1];
      isEven = true;
      
      // A 인접 리스트 채우기
      for (int j = 0; j < E; j++) {
        int start = sc.nextInt();
        int end = sc.nextInt();
        A[start].add(end);
        A[end].add(start);
      }


      // 각 노드에 대해서 DFS 실행 (주어진 그래프가 1개로 연결되어 있다는 보장이 없음)
      for (int j = 1; j <= N; j++) {
        if(isEven)
          DFS(j);
        else // 어느 노드 하나라도 이분 그래프 조건일 충족하지 못한다면 더이상 탐색X
          break;
      }
      
      // 모든 노드에 대해 DFS 탐색한 뒤, 결과 출력
      if (isEven)
        System.out.println("YES");
      else
        System.out.println("NO");

      // 다음 테스트케이스를 위해 check 배열 시작 노드 0으로 초기화 **
      check[1] = 0;
      
    }
  }
  public static void DFS(int node) {
    
    visited[node] = true;
    
    for (int v : A[node]) {
      if (!visited[v]) {
        // 현재 노드와 다른 집합으로 연결 노드 집합 저장(0과 1을 번갈아가면서 저장)**
        check[v] = (check[node] + 1) % 2;
        DFS(v);
      }
      else {
        // 이미 방문한 노드인데, 현재 나의 노드와 같은 집합이면 이분그래프가 아님!
        if (check[node] == check[v])
          isEven = false;
      }
    }
    
  }
}