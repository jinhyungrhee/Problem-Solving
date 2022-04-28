import java.util.*;

class Main{

  
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String str = sc.nextLine();

    int oneToZero = 0;
    int zeroToOne = 0;
    int cnt = 0;
    // 첫번째 원소에 대한 처리 필요 **
    if (str.charAt(0) == '1') { // 시작이 1
      zeroToOne += 1; // 상대 cnt 1 증가시킴 (한번만 바뀌는 경우 대비)
    }
    else { // 시작이 0
      oneToZero += 1;
    }

    for (int i = 0; i < str.length() - 1; i++) {
      int prev = str.charAt(i) - '0';
      int next = str.charAt(i + 1) - '0';
      if (prev != next) {
        if (next == 1) zeroToOne += 1;
        else oneToZero += 1;
      }
    }

    cnt = Math.min(oneToZero, zeroToOne);

    System.out.println(cnt);
  }
}
