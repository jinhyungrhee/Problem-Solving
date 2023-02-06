import java.util.Scanner;

public class AmazingPrimeNumber024 {

	static int N;
		
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		
		// 2, 3, 5, 7
		DFS(2, 1);
		DFS(3, 1);
		DFS(5, 1);
		DFS(7, 1);
		

	}
	
	public static void DFS(int num, int jarisu) {
		
		if (jarisu == N) {
			if (isPrime(num)) {
				System.out.println(num);
			}
			return;
		}
		
		for (int i = 1; i <= 9; i++) {
		
			if (!isPrime((num * 10) + i)) {
				continue;
			}
			
			DFS((num * 10) + i, jarisu + 1);
		}
		
	}
	
	public static boolean isPrime(int num) {
		for (int i = 2; i <= num/2; i++) {
			if (num % i == 0) {
				return false;
			}
		}
		
		return true;
	}

}