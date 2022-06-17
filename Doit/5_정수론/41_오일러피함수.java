import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);
    long n = sc.nextLong(); // 소인수 표현
    long result = n; // 결과값

    // 2 ~ N의 제곱근까지 탐색
    for (int p = 2; p <= Math.sqrt(n); p++) {
      // 현재값이 소인수면
      if (n % p == 0) {
        // 연산을 사용하여 결과값 업데이트 
        result = result - (result / p); 

        // n에서 현재 소인수 내역 제거
        // (2^7*11이라면 2^7을 없애고 11만 남김)
        while (n % p == 0) { 
          n /= p;
        }
      }
    }
    // n이 마지막 소인수일 때 (아직 소인수 구성이 남아있을 때)
    if (n > 1) {
      // 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스
      result = result - (result / n);
    }
    System.out.println(result);
  }
}

