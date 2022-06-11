import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int K = sc.nextInt();
    int[] A = new int[N];
    for (int i = 0 ; i < N; i++) {
      A[i] = sc.nextInt();
    }

    int count = 0;
    for (int i = N - 1; i >= 0; i--) {
      if (A[i] <= K) { // 현재 동전의 가치가 K보다 작거나 같으면 구성에 추가
        count += K / A[i]; // 몫을 count에 더함
        K = K % A[i]; // 나머지를 K값으로 갱신
      }
    }
    System.out.println(count);
  }
}