import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int[][] A = new int[N][2]; // 이차원 배열로 저장
    for (int i = 0; i < N; i++) {
      A[i][0] = sc.nextInt(); // 0번 인덱스 : 시작 시간
      A[i][1] = sc.nextInt(); // 1번 인덱스 : 종료 시간
    }

    // 재정의된 기준으로 정렬
    Arrays.sort(A, new Comparator<int[]>() {
      @Override
      public int compare(int[] S, int[] E) {
        if (S[1] == E[1]) { //(1)종료 시간이 같은 경우,
          return S[0] - E[0]; // 시작 시간 기준으로 정렬(오름차순)
        }
        //(2) 일반적인 경우, 종료시간 기준으로 정렬(오름차순)
        return S[1] - E[1]; 
      }
    });

    int count = 0;
    int end = -1; // 종료지점 초기화
    for (int i = 0; i < N; i++) {
      if (A[i][0] >= end) {
        // 겹치지 않는 다음 회의가 나온 경우, 종료 시간 업데이트
        end = A[i][1];
        count++; // 총 회의 개수 추가
      }
    }
    System.out.println(count);
  }
}

