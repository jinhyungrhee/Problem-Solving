import java.io.*;
import java.util.*;

class Main {  
  
  static ArrayList<cNode>[] A; // 이차원 인접리스트 정의
  static int lcm; // 최소공배수
  static long[] D; // 각 노드값 저장 배열
  static boolean[] visited; // DFS 방문 배열
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int N = sc.nextInt();
    // 초기화
    A = new ArrayList[N];
    D = new long[N];
    visited = new boolean[N];
    for(int i = 0; i < N; i++) {
      A[i] = new ArrayList<cNode>();
    }

    // 입력 받기 + 최소공배수(LCM) 업데이트
    lcm = 1;
    for (int i = 0; i < N - 1; i++) { // (N - 1)개만 입력 받음
      int a = sc.nextInt();
      int b = sc.nextInt();
      int p = sc.nextInt();
      int q = sc.nextInt();

      // 인접리스트 배열에 에지 정보 저장
      A[a].add(new cNode(b, p, q));
      A[b].add(new cNode(a, q, p)); // 비율 반대로 저장 ***

      // '비율'에 대한 최소공배수(LCM) 업데이트
      lcm *= ((p * q) / gcd(p, q)); 
    }

    // 0번 노드에 최소공배수 저장
    D[0] = lcm;
    // 0번 노드(임의의 노드)에서 DFS 수행
    DFS(0);

    // [test] D 출력
    // for (int i = 0 ; i < N; i++) {
    //   System.out.print(D[i] + " ");
    // }
    // System.out.println();

    // [test] A 출력 -> OK
    // for (int i = 0 ; i < N; i++) {
    //   for (int j = 0; j < A[i].size(); j++) {
    //     System.out.print(A[i].get(j).getP() + " ");
    //   }
    //   System.out.println();
    // }
    // System.out.println();
    
    // D 배열 값들의 최대공약수(GCD) 계산
    long GCD = D[0];
    for (int i = 1; i < D.length; i++) {
      GCD = gcd(GCD, D[i]);
    }
    
    // D배열의 각 값을 최대공약수(GCD)로 나눠서 출력
    for (int i = 0; i < D.length; i++) {
      bw.write(Long.toString(D[i]/GCD) + " ");
    }

    bw.flush();
    bw.close();
    

  }

  public static long gcd(long a, long b) {
    if (b == 0)
      return a;
    return gcd(b, a % b);
  }

  public static void DFS(int now) {
    visited[now] = true;
    for (cNode i : A[now]) {
      int next = i.getB();
      if (!visited[next]) {
        // D[next] = D[now] * (i.getQ()/i.getP()); 
        // 괄호 때문에 오답 발생 -> 먼저 계산된 뒤 int로 처리되어 0값으로 계속 바뀐 듯!
        D[next] = D[now] * i.getQ() / i.getP();
        DFS(next);
      }
    }
  }
}

class cNode { // 해당 노드가 input의 a에 해당
  int b;
  int p; 
  int q;
  
  public cNode(int b, int p, int q){
    this.b = b;
    this.p = p;
    this.q = q;
  }

  // 접근자 함수가 없다면?
  public int getB() {
    return b;
  }

  public int getP() {
    return p;
  }

  public int getQ() {
    return q;
  }
  
}