import java.io.*;
import java.util.*;

class Main {
  // 저장 배열과 결과 변수 전역변수로 정의
  public static int[] A;
  public static long result;

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int N = Integer.parseInt(br.readLine());
    A = new int[N]; // 저장 배열 생성(전역변수)
    
    for (int i = 0; i < N; i++) {
      A[i] = Integer.parseInt(br.readLine());
    }
    br.close();

    radix_sort(A, 5);
    for (int i = 0; i < N; i++) {
      bw.write(A[i] + "\n");
    }
    bw.flush();
    bw.close();
  }

  // radix sort 함수
  private static void radix_sort(int[] A, int max_size) {
    int[] output = new int[A.length]; // 임시 정렬을 위한 배열
    int jarisu = 1; // 현재 자릿수 표현
    int count = 0;

    // 로직 부분
    while (count != max_size) { // 최대 자릿수만큼 반복
      int[] bucket = new int[10]; // 0 ~ 9
      for (int i = 0; i < A.length; i++) {
        bucket[(A[i] / jarisu) % 10]++; // 일의 자리부터 시작하여 최종 자리수까지 확인하여 개수 기록
      }
      for (int i = 1; i < 10; i++) {
        bucket[i] += bucket[i - 1]; // 합 배열 공식으로 bucket을 합 배열 형태로 변경(index 계산 위해?) 
      }

      // 현재 자릿수를 기준으로 정렬
      for (int i = A.length - 1; i >= 0; i--) { 
        output[bucket[(A[i] / jarisu) % 10] - 1] = A[i];
        bucket[(A[i] / jarisu) % 10]--; // bucket 비우기
      }

      // 다음 자릿수 이동을 위해 A 배열에 output 데이터 저장
      for (int i = 0; i < A.length; i++) {
        A[i] = output[i];
      }
      // 자릿수 증가시키기
      jarisu *= 10;
      count++;
    }
  }
}