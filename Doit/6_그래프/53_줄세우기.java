import java.io.*;
import java.util.*;

class Main {
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt(); // 노드 개수
    int M = sc.nextInt(); // 에지 개수(=키를 비교한 횟수)

    // 인접리스트 생성(1) -> ArrayList를 원소(DataType)로 갖는 ArrayList(= 이차원 ArrayList)
    ArrayList<ArrayList<Integer>> A = new ArrayList<>();
    for (int i = 0; i <= N; i++) { // 1 ~ N까지 저장하기 위해
      A.add(new ArrayList<>()); // 위에서 이미 ArrayList<Integer>로 정의했기 때문에 안써줘도 됨!
    }
    // 진입차수 배열
    int[] indegree = new int[N + 1];
    for (int i = 0; i < M; i++) {
      int S = sc.nextInt();
      int E = sc.nextInt();
      // A[S].add(E); // 배열(Array)이 아니므로 A[S] 사용 불가
      A.get(S).add(E); 
      indegree[E]++;
    }

    // 인접리스트 생성(2) ->  ArrayList를 원소(DataType)로 갖는 배열(Array)
    
    // ArrayList<Integer>[] B = new ArrayList[N + 1];
    // for (int i = 1; i <= N; i++) {
    //   B[i] = new ArrayList<Integer>();
    // }
    // // 진입차수 배열
    // int[] indegree = new int[N + 1];
    // for (int i = 0; i < M; i++) {
    //   int S = sc.nextInt();
    //   int E = sc.nextInt();
    //   B[S].add(E);
    //   indegree[E]++;
    // }

    // 위상 정렬 배열(Queue)
    Queue<Integer> q = new LinkedList<>();
    for (int i = 1; i <= N; i++) {
      // 진입 차수가 0인 노드 선택 (위상 정렬 배열에 삽입)
      if (indegree[i] == 0) {
        q.add(i); // offer() 동일 => full일 때, 에러 발생 유무 차이
      }
    }

    while (!q.isEmpty()) {
      int now = q.poll();
      System.out.print(now + " ");
      // 현재 노드와 연결된 노드의 진입차수 1 감소
      for (int next : A.get(now)) {
        indegree[next]--;
        // 진입차수가 0이 된 것들 '위상 정렬 배열'에 다시 추가
        if (indegree[next] == 0) {
          q.add(next);
        }
      }
    }
  }
}
