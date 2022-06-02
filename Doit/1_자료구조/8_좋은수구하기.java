import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    int result = 0;
    long[] A = new long[N];

    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      A[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(A); // O(nlogn)

    // 모든 원소에 대해서 수행
    for (int idx = 0; idx < N; idx++) {
      // 변수 초기화
      long k = A[idx];
      int i = 0;
      int j = N - 1;

      while(i < j) {
        if(A[i] + A[j] == k) {
          if(A[i] != k && A[j] != k) {
            result++;
            break;
          } else if (A[i] == k) {
            i++; 
          } else if (A[j] == k) {
            j--;
          }
          /* 예외처리 더 구체적으로 필요!
          else {
            i++;
            j--;
          }
          */
        } else if (A[i] + A[j] < k) {
          i++;
        } else {
          j--;
        }
        
      }
    }
    System.out.println(result);
    br.close();
  }
}