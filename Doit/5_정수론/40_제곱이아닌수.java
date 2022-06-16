import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    long MIN = sc.nextLong();
    long MAX = sc.nextLong();

    // 최댓값과 최솟값의 차이만큼 배열 선언
    boolean[] Check = new boolean[(int) (MAX - MIN + 1)]; // 제곱수 판별 배열

    // 2의 제곱수인 4부터 Max보다 작거나 같은 값까지 반복(제곱수 형태로 증가)
    for (long i = 2; i * i <= MAX; i++) {
      
      long pow = i * i; // 제곱수
      long start_index = MIN / pow; // 시작 인덱스(=최솟값/제곱수)

      if (MIN % pow != 0) { // 나머지가 0이 아니면 1을 더함
        start_index++; // 나머지가 있으면 1을 더해야 MIN보다 큰 제곱수에서 시작됨**
      }

      // 제곱수의 배수 형태로 탐색 (바깥 for문에서 제곱수(pow)값 갱신됨)
      for (long j = start_index; j * pow <= MAX; j++) { // (j * pow)가 MAX보다 작을 때, 최솟값-최댓값 사이의 제곱수임**
        Check[(int) ((j * pow) - MIN)] = true; // 제곱수를 true로 변경(Count배열에 저장)
      }
    }
    
    int count = 0;
    for (int i = 0; i <= MAX - MIN; i++ ){
      if (!Check[i]) {
        count++;
      }
    }

    System.out.println(count);
    
  }
}