public class ConnectedComponent023 {
	
	static ArrayList<Integer>[] A; // ArrayList 배열 생성 
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		A = new ArrayList[N + 1];
		visited = new boolean[N + 1];
		
		for (int i = 0; i < N + 1; i++) {
			A[i] = new ArrayList<Integer>();
		}
		
		for (int i = 0; i < E; i++) {
			
			st = new StringTokenizer(br.readLine());
			
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			
			A[u].add(v);
			A[v].add(u);
			
		}
		//System.out.println(Arrays.toString(A));
		
		int count = 0;
		for (int i = 1; i < N + 1; i++) {
			if (!visited[i]) {
				DFS(i);
				count++;
			}
		}
		
		System.out.println(count);
	}
	
	// DFS
	static void DFS(int v) {
		if (visited[v]) {
			return;
		}
		
		visited[v] = true;
		for (int i : A[v]) {
			if (visited[i] == false) {
				DFS(i);
			}
		}
	}
}
