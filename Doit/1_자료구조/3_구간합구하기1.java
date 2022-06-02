import java.io.*;
import java.util.*;

// 원래 배열 따로 생성하지 않고 합 배열만 두는 경우

class Main{
  
  public static void main(String[] args) throws IOException {

    // Scanner 대신 BufferedReader + StringTokenizer 사용
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine()); // 5 3

    int suNo = Integer.parseInt(stringTokenizer.nextToken()); // 5
    int quizNo = Integer.parseInt(stringTokenizer.nextToken()); // 3

    // 원래 배열(A)은 따로 구현하지 않고 값을 입력 버퍼에 두어서 사용
    long[] S = new long[suNo + 1];

    stringTokenizer = new StringTokenizer(bufferedReader.readLine()); // 5 4 3 2 1
    for (int i = 1; i <= suNo; i++) {
      S[i] = S[i - 1] + Integer.parseInt(stringTokenizer.nextToken());
    }
    for (int q = 0; q < quizNo; q++) {
      stringTokenizer = new StringTokenizer(bufferedReader.readLine()); // 1 3 / 2 4 / 5 5
      int i = Integer.parseInt(stringTokenizer.nextToken());
      int j = Integer.parseInt(stringTokenizer.nextToken());
      System.out.println(S[j] - S[i - 1]);
    }    
  }
}

// 원래 배열, 합 배열 둘 다 생성한 경우

/*
class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int M = sc.nextInt();

    int[] A = new int[N+1];
    int[] S = new int[N+1];

    A[0] = 0;
    S[0] = A[0];
    
    for (int i = 1; i < N + 1; i++) {
      A[i] = sc.nextInt();
      S[i] = S[i - 1] + A[i];
    }

    for (int k = 0; k < M; k++) {
      int i = sc.nextInt();
      int j = sc.nextInt();
      System.out.println(S[j] - S[i - 1]);
    }
  }
}
*/