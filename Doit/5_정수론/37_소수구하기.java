import java.io.*;
import java.util.*;

class Main {  

  static int answer = 0;
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int S = sc.nextInt();
    int N = sc.nextInt();

    int[] A = new int[N + 1];

    for (int i = 2; i <= N; i++) { // 1은 제외
      A[i] = i;
    }

    // 2부터 N의 제곱근까지 탐색 (최적화)
    // => N이 a*b라고 가정했을 때, a와 b 모두 N의 제곱근보다 클 수 없다 **
    for (int i = 2; i <= Math.sqrt(N); i++) {
      if (A[i] == 0) { 
        continue; // 이미 삭제된 것은 건너뜀
      }
      // 현재 인덱스의 배수 모두 지움(값을 0으로 변경)
      for (int j = i + i; j <= N; j = j + i) { // j는 i배로 증가 **
        A[j] = 0;
      }
    }

    // 지워지지 않은 것(=소수)들 출력
    for (int i = S; i <= N; i++) {
      if (A[i] != 0) {
        System.out.println(A[i]);
      }
    }

  }
}
