import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int N = sc.nextInt();
		
		ArrayList<Integer> list = new ArrayList<>(N);
		
		for (int i = 0; i < N; i++) {
			list.add(sc.nextInt());
		} 
		
		Collections.sort(list);
		
		for (int elem : list) {
			sb.append(elem).append("\n");
		}
		
		System.out.println(sb);
		
	}

}

// ref) https://st-lab.tistory.com/106
// 정리하기!