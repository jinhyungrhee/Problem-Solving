import java.util.*;

class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();

    // 입력 값을 String형 변수로 저장한 뒤 char[]형 변수로 변환
    String sNum = sc.next();

    char[] cNum = sNum.toCharArray();

    int sum = 0; // 초기화

    for (int i = 0; i < N; i++) {
      sum += cNum[i] - '0'; // char to int (또는 -48)
    }

    System.out.print(sum);
    
  }
}