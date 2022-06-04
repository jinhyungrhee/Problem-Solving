import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    String str = sc.next();
    int[] A = new int[str.length()];
    
    // substring()을 이용해 숫자를 각 자릿수별로 나눈 후 배열에 저장**
    for (int i = 0; i < str.length(); i++) {
      A[i] = Integer.parseInt(str.substring(i, i+1)); // i번째부터 i+1전까지 자름
    }

    for (int i = 0; i < str.length(); i++) {
      int Max = i;
      for (int j = i + 1 ; j < str.length(); j++) {
        // Max값(= 인덱스) 찾기
        if (A[Max] < A[j])
          Max = j;
      }
      // swap
      if (A[Max] > A[i]) {
        int tmp = A[i];
        A[i] = A[Max];
        A[Max] = tmp;
      }
    }
    for (int i = 0; i < str.length(); i++) {
      System.out.print(A[i]);
    }
  }
}
