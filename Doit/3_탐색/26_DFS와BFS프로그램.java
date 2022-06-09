class Main {  
  static ArrayList<Integer>[] A;
  static boolean[] visited;

  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt(); // 노드 수 
    int M = sc.nextInt(); // 에지 수
    int start = sc.nextInt(); // 시작점

    A = new ArrayList[N + 1];
    for (int i = 1; i <= N; i++) {
      A[i] = new ArrayList<Integer>();
    }

    for (int i = 0; i < M; i++) {
      int s = sc.nextInt();
      int e = sc.nextInt();
      A[s].add(e);
      A[e].add(s);
    }

    // 각 인접 리스트 오름차순 정렬
    for (int i = 1; i <= N; i++) {
      Collections.sort(A[i]);
    }

    visited = new boolean[N + 1];
    DFS(start);
    System.out.println();

    visited = new boolean[N + 1];
    BFS(start);
    System.out.println();

  
  }

  
  static void DFS(int node) {
    System.out.print(node + " ");

    visited[node] = true;

    for (int i : A[node]) {
      if (!visited[i]) {
        DFS(i);
      }
    }
    // return은 따로 안 해도 되나?
  }

  static void BFS(int node) {
    Queue<Integer> q = new LinkedList<>();
    q.add(node);
    visited[node] = true;
    
    while(!q.isEmpty()) {
      int now = q.poll();
      System.out.print(now + " ");
      for (int i : A[now]) {
        if (!visited[i]) {
          visited[i] = true;
          q.add(i);
        }
      }
    }
  }
}
