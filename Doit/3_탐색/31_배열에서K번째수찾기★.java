import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int K = sc.nextInt();

    long start = 1; // 시작 인덱스 1
    long end = K; // 종료 인덱스 K
    long ans = 0; // 

    while (start <= end) {
      long mid = (start + end) / 2; // 중앙값
      // 중앙값보다 작은 수는 몇 개인지 count
      long cnt = 0; 
      // 모든 값을 일일이 생성하고 비교하지 않아도 계산 가능 (패턴 찾기) ***
      for (int i = 1; i <= N; i++) {
        cnt += Math.min(mid / i, N); 
      }

      // 중앙값 조정
      if (cnt < K) { // 현재 중앙값보다 작은 수의 개수(cnt)가 K보다 작은 경우
        start = mid + 1;
      } else { // 현재 중앙값보다 작은 수의 개수(cnt)가 K보다 크거나 같은 경우
        ans = mid; // 그 때의 중앙값 저장 ***
        end = mid - 1; // start > end 될 때까지 계속 조정 ***
      }
    }
    System.out.println(ans);
  }
}

