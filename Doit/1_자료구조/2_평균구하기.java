import java.util.*;

class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();

    int[] arr = new int[N];

    for (int i = 0; i < N; i++) {
      arr[i] = sc.nextInt();
    }

    long max_val = 0;
    long sum_val = 0;
    for (int i = 0; i < N; i++) {
      if (max_val < arr[i]) max_val = arr[i];
      sum_val += arr[i];
    }

    System.out.println((sum_val * 100 / max_val) / N);
    
  }
}