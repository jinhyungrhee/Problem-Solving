import java.io.*;
import java.util.*;

class Main {   

  static int[] parent;
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int M = sc.nextInt();

    // 0 ~ N까지 대표 노드를 저장하는 배열 생성
    parent = new int[N + 1]; 
    // 초기화
    for (int i = 0; i <= N; i++) {
      parent[i] = i;
    }
    
    for (int i = 0; i < M; i++) {
      int OP = sc.nextInt();
      int A = sc.nextInt();
      int B = sc.nextInt();

      if (OP == 0) {
        union(A, B);
      } else {
        if (checkSame(A, B)) {
          System.out.println("YES");
        } else {
          System.out.println("NO");
        }
      }  
    }
  }

  // 두 집합을 합치는 함수(= 대표노드를 하나로 합침)
  public static void union(int a, int b) {
    int rA = find(a);
    int rB = find(b); 

    // (1) 대소 비교하여 작은 수가 대표노드가 되도록 지정함
    // if (rA < rB)
    //   parent[rB] = rA;
    // else
    //   parent[rA] = rB;

    // =>(1) parent 배열 결과
    // 1 2 3 4 5 6 7
    // 1 2 1 2 5 1 6
    // =>/ [1] 3 6 7 / [2] 4 / [5] /

    // (2) 두 원소의 대표 노드끼리 연결 (왜 대소 비교가 필요없는가?)
    // Q. 왜 rA와 rB가 다르면, 대소 비교 없이 단순히 rB가 rA를 가리키도록 설정하는 것이 가능한가? 
    if (rA != rB) {
      parent[rB] = rA;
    }

    // =>(2) parent 배열 결과
    // 1 2 3 4 5 6 7
    // 1 4 1 4 5 7 1 
    // =>/ [1] 3 6 7 / 2 [4] / [5] /

    // **(결론)**
    // (1)번을 택하든 (2)번을 택하든 집합의 포함관계는 동일함 -> 따라서 해당 문제에서는 별 다른 에러 없이 통과된 것!
    // (1)번 방법을 선택하면 대표노드가 해당 집합에서 가장 작은 수로 설정됨
    // (2)번 방법을 선택하면 별다른 규칙 없이 대표노드가 설정됨
  }

  // 대표 노드 찾는 함수 (재귀함수로 구현)
  public static int find(int a) {
    if (parent[a] == a)
      return a;
    else
      return parent[a] = find(parent[a]); // 경로 압축 ***
  }

  // 두 원소가 같은 집합인지 확인하는 함수
  public static boolean checkSame(int a, int b) {
    int rA = find(a);
    int rB = find(b);

    if (rA == rB)
      return true;
    else
      return false;
  }
}
