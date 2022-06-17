import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    long a = Long.parseLong(st.nextToken());
    long b = Long.parseLong(st.nextToken());

    long result = gcd(a, b);

    // 출력 횟수가 많은 경우, 일반적인 출력을 수행하면 시간초과 발생
    // -> BufferedWriter 사용!

    for (int i = 0; i < result; i++) {
      bw.write("1"); //  bw : 출력 버퍼로 버퍼링된 "문자형" 출력 스트림 객체 => 1(X), "1"(O)
    }
    
    bw.flush();
    bw.close();

  }

  public static long gcd(long a, long b) {
    if (b == 0) {
      return a;
    }
    return gcd(b, a % b); 
  }
}

