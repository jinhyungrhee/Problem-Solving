import java.io.*;
import java.util.*;

class Main {

  public static int[] A, tmp;
  public static long result;
  
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    
    A = new int[N + 1];
    tmp = new int[N + 1];

    for (int i = 1; i <= N; i++) {
      A[i] = Integer.parseInt(br.readLine());
    }

    result = 0;
    // 병합 정렬 수행
    merge_sort(1, N);
    System.out.println(result);
    
  }

  private static void merge_sort(int s, int e) {
    if (e - s < 1) return; // 바닥 조건 : 시작점과 끝점이 만날 경우
    
    int m = s + (e - s) / 2; // 중간 값

    // 재귀형태
    merge_sort(s, m);
    merge_sort(m + 1, e);

    // 끝까지 타고 내려간 뒤 tmp배열에 범위(s-e) 저장
    for (int i = s; i <= e; i++) {
      tmp[i] = A[i];
    }

    int k = s; // 전체 인덱스를 관리하기 위한 변수 k
    int index1 = s;
    int index2 = m + 1;

    // 두 그룹을 병합하는 로직
    while (index1 <= m && index2 <= e) {
      // 두 그룹의 각 원소 차례로 비교
      if (tmp[index1] > tmp[index2]) { // 뒤쪽 데이터 값이 작은 경우
        A[k] = tmp[index2];
        // result 업데이트 (index가 앞으로 이동한 만큼 추가) => 기존 merge_sort코드에서 이 부분만 추가!**
        result += index2 - k;
        k++;
        index2++;
      } else { // 뒤쪽 데이터 값이 큰 경우
        A[k] = tmp[index1];
        k++;
        index1++;
      }
    }
    // 반복문이 끝난 후 남아있는 데이터 정리
    while (index1 <= m) {
      A[k] = tmp[index1];
      k++;
      index1++;
    }
    while (index2 <= e) {
      A[k] = tmp[index2];
      k++;
      index2++;
    }
  }
}
