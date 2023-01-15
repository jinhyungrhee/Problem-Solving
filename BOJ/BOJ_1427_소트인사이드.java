import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String num = sc.next();
		int N = num.length();
		int[] A = new int[N];
		
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(num.substring(i, i+1));
		}
		
		// selection sort (Descending Number)
		for (int i = 0; i < N; i++) {
			
			// 뒤에서부터 비교하는 숫자의 자리까지 오면서 최댓값 찾기
			int max = i;
			for (int j = N-1; j > i; j--) {
				if (A[j] > A[max]) {
					max = j;
				}
			}
			
			// 최댓값이 비교하는 자리보다 크면 swap (-> 맨 앞자리부터 정렬)
			if (A[i] < A[max]) {
				int temp = A[i];
				A[i] = A[max];
				A[max] = temp;
			}
			
			
		}
		
		//System.out.println(Arrays.toString(A));
		for (int elem : A) {
			System.out.print(elem);
		}
		
	}

}