import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int[] A = new int[N];

    for (int i = 0; i < N; i++) {
      A[i] = sc.nextInt();
    }
    Stack<Integer> stack = new Stack<>();

    // 우선 버퍼에 저장 후 한꺼번에 출력하기 위해 StringBuffer 사용
    StringBuffer bf = new StringBuffer();
    // 오름차순 수
    int num = 1;

    boolean result = true;

    for (int i = 0; i < A.length; i++) {
      int su = A[i]; // 현재 수열의 수
      // 현재 수열 값 >= 오름차순 자연수 : 값이 같아질 때까지 push() 수행
      if (su >= num) {
        while (su >= num) {
        stack.push(num++);
        bf.append("+\n");
        }
        stack.pop(); // 마지막에 한 번 pop()하여 현재 수열 값 출력
        bf.append("-\n");
      
      } 
      else { // 현재 수열 값 < 오름차순 자연수 : pop() 수행하여 수열 원소 꺼냄
        int n = stack.pop();
        // 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면, 수열 출력 불가
        if (n > su) {
          System.out.println("NO");
          result = false;
          break;
        }
        // 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 작으면, pop() 버퍼에 기록
        else {
          bf.append("-\n");
        }
      }
    }
    // 한번이라도 NO가 출력된 적이 없으면(result == true), 버퍼 한꺼번에 출력
    if (result) System.out.println(bf.toString());
  }
}