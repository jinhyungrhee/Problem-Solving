import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();

    int[] A = new int[1000001];

    for (int i = 2; i < A.length; i++) {
      A[i] = i; // 배열 초기화
    }

    // 에라토스테네스의 체
    for (int i = 2; i <= Math.sqrt(A.length); i++) { // 배열의 제곱근까지만 수행
      if (A[i] == 0) { // 소수가 아니면 스킵
        continue;
      }
      // 배수 제거
      for (int j = i + i; j < A.length; j = j + i) { // 2~1000000까지 반복
        A[j] = 0;
      }
    }
    
    // 팰린드롬 판별
    int i = N; // 입력받은 수부터 탐색 시작(초기 인덱스)
    while (true) {
      if (A[i] != 0) { // 소수에 대해서 팰린드롬 체크
        int result = A[i];
        if (isPalindrome(result)) {
          System.out.println(result);
          break;
        }
      }
      i++; // 인덱스 1씩 증가시키며 차례로 비교
    }
  }
  
  // 팰린드롬 판별 함수
  private static boolean isPalindrome(int target) {
    char[] temp = String.valueOf(target).toCharArray();
    // 투포인터
    int s = 0;
    int e = temp.length - 1;
    while (s < e) { // 두 인덱스가 교차할 때까지
      if (temp[s] != temp[e]) {
        return false;
      }
      s++;
      e--;
    } 
    return true;
  }
}
