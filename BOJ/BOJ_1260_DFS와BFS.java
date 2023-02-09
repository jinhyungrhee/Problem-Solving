import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	static ArrayList<Integer>[] A;
	static boolean[] visited;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int start = sc.nextInt();
		
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
		
		for (int i = 1; i <= N; i++) {
			Collections.sort(A[i]);
		}

		//System.out.println(Arrays.toString(A));
		
		visited = new boolean[N+1];
		DFS(start);
		System.out.println();
		visited = new boolean[N+1];
		BFS(start);
		
		
	}
	
	public static void DFS(int node) {
		
 		visited[node] = true;
		System.out.print(node + " ");
		
		for (int v : A[node]) {
			if (!visited[v]) {
				//visited[v] = true;
				DFS(v);
			}
		}
		
	}
	
	public static void BFS(int node) {
		
		Queue<Integer> queue = new LinkedList<>();
		queue.add(node);
		visited[node] = true;
		
		while(!queue.isEmpty()) {
			
			int now = queue.poll();
			
			System.out.print(now + " ");
			
			for (int v : A[now]) {	
				if (!visited[v]) {
					visited[v] = true;
					queue.add(v);
				}
			}
			
		}
	}

}