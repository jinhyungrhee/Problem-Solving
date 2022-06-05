import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();

    int[] A = new int[N];
    int[] S = new int[N];

    for (int i = 0; i < N; i++) {
      A[i] = sc.nextInt();
    }

    // 삽입 정렬
    for (int i = 1; i < N; i++) {
      int insert_point = i;
      int insert_value = A[i];
      for (int j = i - 1 ; j >= 0; j--) { // j는 뒤에서부터 반복
        if(A[j] < A[i]) {
          insert_point = j + 1;
          break;
        }
        if (j == 0) {
          insert_point = 0;
        }
      }
      // 삽입을 위해 삽입 위치에서 i까지 데이터를 한 칸씩 뒤로 밀기
      for (int j = i; j > insert_point; j--) { // j는 뒤에서부터 반복
        A[j] = A[j - 1];
      }
      // 삽입 위치에 현재 데이터 삽입
      A[insert_point] = insert_value;
    }
    // 합 배열 만들기
    S[0] = A[0];
    for (int i = 1; i < N; i++) {
      S[i] = S[i - 1] + A[i];
    }
    // 합 배열 총합 구하기
    int sum = 0;
    for (int i = 0; i < N; i++) {
      sum += S[i];
    }
    System.out.println(sum);
  }
}
