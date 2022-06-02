import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt(); // 입력 숫자 개수
    int M = sc.nextInt(); // 나눌 수

    // 합 배열 선언
    long[] S = new long[N];
    
    // 같은 나머지의 인덱스 카운트하는 배열
    long[] C = new long[M];

    long answer = 0;
    S[0] = sc.nextInt();
    // 합 배열 채우기
    for (int i = 1; i < N; i++) {
      S[i] = S[i - 1] + sc.nextInt();
    }

    // 합 배열의 모든 값에 mod 연산 수행
    for (int i = 0; i < N; i++) {
      int remainder = (int) (S[i] % M);
      // 0 ~ i 구간 합이 0일 때 정답에 추가
      if (remainder == 0) answer++;
      // 나머지가 같은 인덱스 개수 카운트
      C[remainder]++;
    }

    for (int i = 0; i < M; i++) {
      // 두 개를 뽑을 수 있는 경우에 대하여
      if (C[i] > 1) {
        // C[i]개 중 2개를 뽑는 경우의 수 구하는 공식 : C[i] * (C[i] - 1) / 2
        answer = answer + (C[i] * (C[i] - 1) / 2);
      }
    }
    System.out.println(answer);
    
  }
}

/*
[입력]
5 3 
1 2 3 1 2

[출력]
7
*/