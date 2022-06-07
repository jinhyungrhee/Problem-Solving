import java.io.*;
import java.util.*;

class Main{
  // 전역 변수 정의
  public static int[] A, tmp;
  public static long result;
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int N = Integer.parseInt(br.readLine());
    // 배열 A와 배열 tmp는 전역 변수
    A = new int[N + 1];
    tmp = new int[N + 1];
    for (int i = 1; i <= N; i++) {
      A[i] = Integer.parseInt(br.readLine());
    }

    // 병합 정렬 수행
    merge_sort(1, N);

    // 결과 출력
    for (int i = 1; i <= N; i++) {
      bw.write(A[i] + "\n");
    }
    bw.flush();
    bw.close();
    
  }
  // 병합 정렬 함수 구현
  private static void merge_sort(int s, int e) {
    if (e  - s < 1) return; // 종료 조건

    // 중간값 구하기
    // int m = (s + e) / 2;
    int m = s + (e - s) / 2; // 결과가 동일한 이유는?

    // 재귀 함수 형태로 구현
    merge_sort(s, m);
    merge_sort(m + 1, e);
    // s~e까지 임시 배열에 저장
    for (int i = s; i <= e; i++) {
      tmp[i] = A[i];
    }

    int k = s; // k는 선택된 데이터의 인덱스
    int idx1 = s; // 앞쪽 그룹 시작점
    int idx2 = m + 1; // 뒤쪽 그룹 시작점

    // 두 그룹을 병합하는 로직
    while (idx1 <= m && idx2 <= e) {
      // 양쪽 그룹의 index가 가리키는 값을 비교해 더 작은 수를 선택해 배열에 저장 후
      // 선택된 데이터의 index값을 오른쪽으로 한 칸 이동
      if (tmp[idx1] > tmp[idx2]) {
        A[k] = tmp[idx2];
        k++;
        idx2++;
      } else {
        A[k] = tmp[idx1];
        k++;
        idx1++;
      }
    }
    // 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
    while (idx1 <= m) {
      A[k] = tmp[idx1];
      k++;
      idx1++;
    }
    while (idx2 <= e) {
      A[k] = tmp[idx2];
      k++;
      idx2++;
    }
    
  }
  
}
