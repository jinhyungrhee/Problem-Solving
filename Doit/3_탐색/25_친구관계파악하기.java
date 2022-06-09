import java.io.*;
import java.util.*;

class Main {
  // 전역 변수로 정의
  static ArrayList<Integer>[] A;
  static boolean[] visited;
  static boolean arrive;

  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt(); // 노드 수
    int M = sc.nextInt(); // 에지 수

    arrive = false;
    visited = new boolean[N];
    // 2차원 연결리스트 생성 및 초기화
    A = new ArrayList[N];
    for (int i = 0; i < N; i++) {
      A[i] = new ArrayList<Integer>();
    }

    // 입력받은 정보 저장
    for (int i = 0; i < M; i++) {
      int s = sc.nextInt();
      int e = sc.nextInt();
      A[s].add(e);
      A[e].add(s);
    }

    // 각 노드마다 DFS 실행
    for (int i = 0; i < N; i++) {
      DFS(i, 1);
      if (arrive) { // depth == 5에 도달한 적이 있다면 반복문 종료
        break;
      }
    }

    // 존재 유무 판별하여 결과 출력
    if (arrive) {
      System.out.println("1");
    } else {
      System.out.println("0");
    }
  }
  
  static void DFS(int now, int depth) {
    if (depth == 5 || arrive) { // depth == 5가 되면 프로그램 종료
      arrive = true;
      return;
    }

    // 그렇지 않으면, 방문 배열에 현재 노드 방문 기록
    visited[now] = true;
    // 연결 노드 중 방문하지 않은 노드 DFS 실행 (호출마다 depth 1씩 증가)
    for (int i : A[now]) {
      if (!visited[i]) {
        DFS(i, depth + 1);
      }
    }

    // backtrack**
    // depth == 5에 도달하지 못하면 다시 return되어 마지막에 false 기록 (원상복구)
    visited[now] = false;
  }

}
