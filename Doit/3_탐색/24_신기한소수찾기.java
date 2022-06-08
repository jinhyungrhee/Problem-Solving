import java.io.*;
import java.util.*;

class Main {
  // 전역 변수로 정의
  static int N;

  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);
    N = sc.nextInt();
    
    // 일의 자리 소수 4개로부터 시작
    DFS(2, 1);
    DFS(3, 1);
    DFS(5, 1);
    DFS(7, 1);
  }
  
  private static void DFS(int number, int jarisu) {
    if (jarisu == N) {
      if (isPrime(number)) {
        System.out.println(number);
      }
      // 소수가 아니면 그냥 리턴
      return;
    }
    for (int i = 1; i < 10; i++) {
      // 짝수면 더 이상 탐색할 필요가 없음
      if (i % 2 == 0) {
        continue;
      }
      if (isPrime(number * 10 + i)) { // 다음 자리수 포함한 숫자가 소수라면 DFS 진행
        DFS(number * 10 + i, jarisu + 1); // DFS(해당 숫자, 자리수 + 1)
      }
    }
  }

  // 간단한 소수 판별 함수
  private static boolean isPrime(int num) {
    for (int i = 2; i <= num / 2; i++) { // Q.(num / 2)까지만 탐색해도 충분한 이유?
      if (num % i == 0)
        return false;
    }
    return true;
  }
}