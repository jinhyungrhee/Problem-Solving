import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class DiameterOfTree028 {

	static ArrayList<Node>[] A;
	static boolean[] visited;
	static int[] distance;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		A = new ArrayList[N+1];
		// 인접 리스트 초기화
		for (int i = 1; i <= N; i++) {
			A[i] = new ArrayList<Node>();
		}    
		
		//System.out.println(Arrays.toString(A));
		
		// 입력
		
		for (int i = 0; i < N; i++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
		
			int S = Integer.parseInt(st.nextToken());
			
			while(true) {
								
				int E = Integer.parseInt(st.nextToken());
				if (E == -1) break;
				
				int V = Integer.parseInt(st.nextToken());
				
				A[S].add(new Node(E, V));
				
			}
			
		}
		
		visited = new boolean[N+1];
		distance = new int[N + 1];
		BFS(1);
		
		int maxIndex = 1;
		for (int i = 2; i <= N; i++) {
			if (distance[maxIndex] < distance[i]) {
				maxIndex = i;
			}
		}
		
		visited = new boolean[N+1];
		distance = new int[N + 1];
		BFS(maxIndex);
		
		Arrays.sort(distance);
		
		System.out.println(distance[N]);
		
	}
	
	public static void BFS(int index) {
		
		Queue<Integer> queue = new LinkedList<>();
		queue.add(index);
		visited[index] = true;
		
		while(!queue.isEmpty()) {
			
			int now = queue.poll();
			
			for (Node v : A[now]) {
				
				if (!visited[v.edge]) {
					visited[v.edge] = true;
					queue.add(v.edge);
					distance[v.edge] = distance[now] + v.value;
				}
				
			}
			
		}

		
	}

}

class Node {
	
	int edge;
	int value;
	
	public Node(int edge, int value) {
		this.edge = edge;
		this.value = value;
	}
	
	
	@Override
	public String toString() {
		return "(" + this.edge + " : " + this.value + ")";
	}
}

/*

public class DiameterOfTree028 {

	static ArrayList<Node>[] A;
	static boolean[] visited;
	static int sumValue;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		A = new ArrayList[N+1];
		visited = new boolean[N+1];
		sumValue = 0;
		// 인접 리스트 초기화
		for (int i = 1; i <= N; i++) {
			A[i] = new ArrayList<Node>();
			visited[i] = false;
		}
		
		
		// 입력
		
		for (int i = 0; i < N; i++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
		
			int S = Integer.parseInt(st.nextToken());
			
			while(true) {
								
				int E = Integer.parseInt(st.nextToken());
				if (E == -1) break;
				
				int V = Integer.parseInt(st.nextToken());
				
				A[S].add(new Node(E, V));
				
			}
			
		}
		
		
		int maxLength = 0;
		// 모든 노드에서 BFS 실행하여 가장 긴 값 체크
		for (int i = 1; i <= N; i++) {
			BFS(i);
			if (sumValue > maxLength) {
				maxLength = sumValue;
			}
			// sumValue 초기화
			sumValue = 0;
			// visited 배열 초기화
			for (int j = 1; j < N; j++) {
				visited[j] = false;
			}
			
		}
		
		System.out.println(maxLength);
		
	}
	
	public static void BFS(int index) {
		
		Queue<Integer> queue = new LinkedList<>();
		queue.add(index);
		visited[index] = true;
		
		while(!queue.isEmpty()) {
			
			int now = queue.poll();
			
			for (Node v : A[now]) {
				
				if (!visited[v.edge]) {
					sumValue += v.value;
					visited[v.edge] = true;
					queue.add(v.edge);
				}
				
			}
			
		}
	}

}

class Node {
	
	int edge;
	int value;
	
	public Node(int edge, int value) {
		this.edge = edge;
		this.value = value;
	}
	
	
	@Override
	public String toString() {
		return "(" + this.edge + " : " + this.value + ")";
	}
}

*/