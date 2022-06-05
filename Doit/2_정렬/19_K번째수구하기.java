import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st  = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());
    int[] A = new int[N];

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      A[i] = Integer.parseInt(st.nextToken());
    }

    // quick sort 실행
    quickSort(A, 0, N - 1, K - 1);
    // 정렬된 K번째 수 출력
    System.out.println(A[K - 1]);
    
  }
  // quick sort 함수 구현
  public static void quickSort(int[] A, int S, int E, int K) {
    if (S < E) {
      // pivot 구하기
      int pivot = partition(A, S, E);
      // K번째 수가 pivot이면 더 이상 구할 필요 없음
      if (pivot == K) return;
      // K가 pivot보다 작으면, 왼쪽 그룹만 정렬 수행
      else if (K < pivot) quickSort(A, S, pivot - 1, K);
      // K가 pivot보다 크면, 오른쪽 그룹만 정렬 수행
      else quickSort(A, pivot + 1, E, K);      
    }
  }

  // 피벗 구하기 함수 구현
  public static int partition(int[] A, int S, int E) {
    
    int M = (S + E) / 2; // 중앙값 찾기
    swap(A, S, M); // 중앙값을 1번째 요소로 이동
    int pivot = A[S]; // 맨 앞으로 이동한 중앙값을 피봇으로 설정(i,j이동이 편하도록)

    int i = S, j = E;
    
    while (i < j) {
      // 피벗보다 작은 수가 나올 때까지 j--
      while (pivot < A[j]) {
        j--;
      }
      // 피벗보다 큰 수가 나올 때까지 i++
      while (i < j && pivot >= A[i]) {
        i++;
      }
      // 찾은 i와 j를 swap
      swap(A, i, j);
    }
    // i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정**
    A[S] = A[i];
    A[i] = pivot;
    return i;
  }
  // swap 함수 구현
  public static void swap(int[] A, int i, int j) {
    int tmp = A[i];
    A[i] = A[j];
    A[j] = tmp;
  }
}
