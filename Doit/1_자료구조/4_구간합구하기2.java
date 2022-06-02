import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine()); // 4 3 

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    // 원본 배열 저장
    int A[][] = new int[N + 1][N + 1];
    for (int i = 1; i <= N; i++) {
      st = new StringTokenizer(br.readLine()); // 1 2 3 4 / 2 3 4 5 / 3 4 5 6 / 4 5 6 7
      for (int j = 1; j <= N; j++) {
        A[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    // 구간 합 배열 계산 (어차피 구간합 배열의 0행, 0열은 0이므로 저절로 1행, 1열이 초기화됨 -> 초기화 코드 필요X)
    int D[][] = new int[N + 1][N + 1];
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j];
      }
    }

    // 출력
    /*
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        System.out.print(D[i][j] + " ");
      }
      System.out.println();
    }
    */

    // 특정 범위의 구간 합 구하기
    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int x1 = Integer.parseInt(st.nextToken());
      int y1 = Integer.parseInt(st.nextToken());
      int x2 = Integer.parseInt(st.nextToken());
      int y2 = Integer.parseInt(st.nextToken());

      int result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1];
      System.out.println(result);
    }
    
  }
}