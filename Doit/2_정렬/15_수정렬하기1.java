import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int[] A = new int[N];
    
    for (int i = 0; i < N; i++) {
      A[i] = sc.nextInt();
    }

    for (int i = 0; i < N - 1; i++) {
      for (int j = 0; j < N - 1 - i; j++) {
        // 두 수를 비교하여, 앞의 수가 더 크면 swap
        if (A[j] > A[j + 1]) {
          int tmp = A[j];
          A[j] = A[j + 1];
          A[j + 1]  = tmp;
        }
      }
    }
    // 출력
    for (int i = 0; i < N; i++) {
      System.out.println(A[i]);
    }
  }
}