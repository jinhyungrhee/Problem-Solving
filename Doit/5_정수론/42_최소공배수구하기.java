import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();

    for (int i = 0; i < T; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      // 최소공배수(LCM) = A * B / 최대공약수(GCD)
      int LCM = a * b / gcd(a, b);

      System.out.println(LCM);
    }
  }

  // 최대공약수 구하기(유클리드 호제법)
  // 큰수 작은수 구분을 하지 않아도 되는 이유? 
  // -> 로직에 따라 MOD연산결과(=두수의 차)가 다음 연산에서 작은 수로 가기 때문에 큰수 작은수 구분 필요X
  public static int gcd(int a, int b) {

    // 작은 수가 0이 되면 종료
    if (b == 0) {
      return a;
    }
    // 재귀 호출 (다음 번에는 작은 수가 큰 수가 되고 MOD연산 결과가 작은 수가 됨)
    return gcd(b, a % b); 
    
  }
}

