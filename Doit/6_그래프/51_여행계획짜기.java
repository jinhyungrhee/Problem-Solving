import java.io.*;
import java.util.*;

class Main {

  static int[] parent;
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int M = sc.nextInt();

    int[][] dosi = new int[N + 1][N + 1];
    int[] route = new int[M + 1];

    // 그래프를 '인접 행렬'로 저장
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        dosi[i][j] = sc.nextInt();
      }
    }

    for (int i = 1; i <= M; i++) {
      route[i] = sc.nextInt();
    }

    // 대표 노드 초기화
    parent = new int[N + 1];
    for (int i = 1; i <= N; i++) {
      parent[i] = i;
    }

    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        if (dosi[i][j] == 1) {
          union(i, j);
        }
      }
    }

    // route 노드들의 대표가 모두 동일한지 체크
    int index = find(route[1]);
    for (int i = 2; i <= M; i++) {
      if(index != find(route[i])) {
        System.out.println("NO");
        return; // 프로그램 종료
      }
    }
    System.out.println("YES");

    // test출력
    // for (int i = 1; i <= N; i++) {
    //   System.out.print(parent[i] + " ");
    // }
    
  }
  public static void union(int a, int b) {
    int rA = find(a);
    int rB = find(b);

    // 두 원소의 대표 노드끼리 연결(규칙X)
    // if (rA != rB) {
    //   parent[rB] = rA;
    // }

    // 항상 큰 도시가 대표가 되도록 설정
    if (rA > rB) {
      parent[rB] = rA;
    } else {
      parent[rA] = rB;
    }
    
  }
  public static int find(int a) {
    if (parent[a] == a) {
      return a;
    } else {
      return parent[a] = find(parent[a]); // 경로 압축
    }
  }
}
