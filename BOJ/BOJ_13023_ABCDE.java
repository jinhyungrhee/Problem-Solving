import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static ArrayList<Integer>[] A;
	static boolean[] visited;
	//static int count;
	static boolean isArrived;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		A = new ArrayList[N];
		visited = new boolean[N];
		//count = 1;
		
		for (int i = 0; i < N; i++) {
			A[i] = new ArrayList<Integer>();
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			
			A[s].add(e);
			A[e].add(s);
			
		}

		//System.out.println(Arrays.toString(A));
		
		for (int i = 0; i < N; i++) {
			
			DFS(i, 1);
			// DFS로 끝까지 내려갔다 왔을 때의 depth가 5이면 isArrived가 true가 되고, 더 이상 탐색하지 않아도 됨!
			if (isArrived) {
				break;
			}
	
		}
		
		if (isArrived) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
		
	}
	
	public static void DFS(int num, int depth) {
		
		if (depth == 5 || isArrived) {
			isArrived = true;
			return;
		}
		
		//System.out.println(depth);
		
		visited[num] = true;
		if (visited[num]) {
	
			for (int v : A[num]) {
				//visited[v] = true;
				DFS(v, depth + 1);
			}
		
		}
		visited[num] = false;
		
	}

}