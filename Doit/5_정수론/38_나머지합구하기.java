import java.io.*;
import java.util.*;

class Main {  

  static int answer = 0;
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    long MIN = sc.nextInt();
    long MAX = sc.nextInt();

    long[] A = new long[10000001]; // 10^14의 제곱근인 10^7까지 탐색 필요
    // 배열 초기화
    for (int i = 2; i < A.length; i++) {
      A[i] = i;
    }

    // ================ 에라토스테네스체를 사용한 소수 판별 ================================
    
    for (int i = 2; i < Math.sqrt(A.length); i++) { // 10^7의 제곱근까지만 탐색
      if (A[i] == 0) {
        continue; // 소수가 아니면 넘어감
      }
      // 배수 지우기
      for (int j = i + i; j < A.length; j = j + i) {
        A[j] = 0;
      } 
    }

    // ================================================================================
    
    int count = 0;
    for (int i = 2; i < 10000001; i++) { // 2~10000000
      if (A[i] != 0) { // 소수인 값에 대해
        long temp = A[i]; // 현재 소수
        // N^k와 B(MAX)를 비교 X => long형 초과 가능(에러 발생)
        // N과 B(MAX)/N^k-1 비교 O 
        while ((double)A[i] <= (double)MAX/(double)temp) {// 각 소수에 관해 소수를 N제곱한 값이 B보다 커질 때까지 반복문 실행 
          if ((double)A[i] >= (double)MIN/(double)temp) {// 소수를 NN제곱한 값이 A보다 크거나 같으면 소수로 판단
            count++;
          }
          temp = temp * A[i];
        }
        
      }
    }
    System.out.println(count);
  }
}

