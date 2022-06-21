import java.io.*;
import java.util.*;

class Main {

  static int[] parent;
  static int[] trueP; // 진실을 아는 사람들
  static ArrayList<Integer>[] party; // 파티정보(인접리스트 사용)
  static int result;
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt(); // 사람수
    int M = sc.nextInt(); // 파티수

    int T = sc.nextInt(); // 진실을 아는 사람수
    trueP = new int[T];
    for (int i = 0; i < T; i++) {
      trueP[i] = sc.nextInt();
    }

    // party 인접리스트 생성 및 초기화
    party = new ArrayList[M];
    for (int i = 0; i < M; i++) {
      party[i] = new ArrayList<Integer>();
    }

    // party 정보 저장
    for (int i = 0; i < M; i++) {
      int num = sc.nextInt();
      for (int j = 0; j < num; j++) {
        party[i].add(sc.nextInt());
      }
    }

    // 대표 노드 배열 초기화
    parent = new int[N + 1];
    for (int i = 1; i <= N; i++) {
      parent[i] = i;
    }

    // 파티 배열(인접리스트)을 돌면서 각 파티의 대표노드를 갱신
    for (int i = 0; i < M; i++) {
      int firstPerson = party[i].get(0);
      for (int j = 1; j < party[i].size(); j++) {
        union(firstPerson, party[i].get(j));
      }
    }

    // 각 파티 대표 노드(cur)와 진실을 아는 사람들의 대표 노드가 같다면 과정 불가 ***
    for (int i = 0; i < M; i++) {
      boolean isPossible = true;
      int cur = party[i].get(0); // party마다 아무노드나 잡아도 find()를 적용하면 대표 노드가 나오므로 get(0)으로 통일!
      for (int j = 0; j < trueP.length; j++) {
        if (find(cur) == find(trueP[j])) {
          isPossible = false;
          break;
        }
      }
      if (isPossible) result++;
    }

    System.out.println(result);
  }

  public static void union(int a, int b) {
    int rA = find(a);
    int rB = find(b);

    if (rA != rB) {
      parent[rB] = rA;
    }
    
  }

  public static int find(int a) {
    if (parent[a] == a) {
      return a;
    } else {
      return parent[a] = find(parent[a]); // 경로 단축
    }
  }

  // 두 원소가 같은 집합인지 확인
  // public static boolean checkSame(int a, int b) {
  //   int rA = find(a);
  //   int rB = find(b);

  //   if (rA == rB) 
  //     return true;
  //   else
  //     return false;
  // }
}
