import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < tc; i++) { 
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int[] arr =  new int[N];
			for (int j = 0; j < N; j++) { // n
				arr[j] = Integer.parseInt(st.nextToken());
			}
			
			double avg = Arrays.stream(arr).sum() / N;
			
			int count = 0;
			for (int j = 0; j < N; j++) {
				if (arr[j] > avg) {
					count++;
				}
			}
			
			double result = count / (double)N * 100;
			System.out.printf("%.3f%%\n", result);
		}
		
	}

}
