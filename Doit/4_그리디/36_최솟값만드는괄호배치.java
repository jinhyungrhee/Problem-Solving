import java.io.*;
import java.util.*;

class Main {  

  static int answer = 0;
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    String example = sc.nextLine();
    // 입력받은 String을 "-" 기준으로 split해서 String배열에 저장
    String[] str = example.split("-");
    for (int i = 0 ; i < str.length; i++) {
      int tmp = mySum(str[i]);
      // 첫 값이면 더함
      if (i == 0) {
        answer = answer + tmp;
      } else { // 나머지는 뺌
        answer = answer - tmp; 
      }
    }
    System.out.println(answer);
    
  }

  static int mySum(String example) {
    String[] str = example.split("\\+"); //split("+")가 에러나는 이유? -> +, *, ^는 특별한 의미로 사용되기 때문!
    int sum = 0;
    for (int i = 0; i < str.length; i++) {
      sum = sum + Integer.parseInt(str[i]);
    }

    return sum;
  }
}

