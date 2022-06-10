import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int[] A = new int[N];
    for (int i = 0; i < N; i++) {
      A[i] = sc.nextInt();
    }

    Arrays.sort(A); // 이진탐색을 위한 오름차순 정렬

    int M = sc.nextInt();
    for (int i = 0; i < M; i++) {
      int target = sc.nextInt();

      boolean find = false;
      int start = 0;
      int end = A.length - 1;
      
      while(start <= end) {
        int mid_idx = (start + end) / 2;
        int mid_val = A[mid_idx];
        if (target > mid_val) {
          start = mid_idx + 1;
        } else if (target < mid_val) {
          end = mid_idx - 1;
        } else { // target == mid
          find = true;
          break;
        }
      }
      if (find) {
        System.out.println("1");
      } else {
        System.out.println("0");
      }
      
    }
  }

}

