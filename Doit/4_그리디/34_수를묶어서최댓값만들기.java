import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();

    PriorityQueue<Integer> plusq = new PriorityQueue<>(Collections.reverseOrder()); // 양수 우선순위 큐(내림차순)
    PriorityQueue<Integer> minusq = new PriorityQueue<>(); // 음수 우선순위 큐(오름차순)

    int one = 0; // 1 개수 카운트
    int zero = 0; // 0 개수 카운트

    // (1) 유형 나누기
    for (int i = 0; i < N; i++) {
      int data = sc.nextInt();
      if (data > 1) {
        plusq.add(data);
      } else if (data == 1) {
        one++;
      } else if (data == 0) {
        zero++;
      } else { // data < 1
        minusq.add(data);
      }
    }

    int sum = 0;
    
    // (2) 양수 처리하기
    while (plusq.size() > 1) { // 큐 크기가 2보다 작을 때까지 반복(0 or 1)
      int first = plusq.remove();
      int second = plusq.remove();
      sum = sum + first * second;
    }
    if (!plusq.isEmpty()) { // 하나만 남아 있으면 sum에 더함
      sum = sum + plusq.remove();
    }

    // (3) 음수 처리하기
    while (minusq.size() > 1) { // 큐 크기가 2보다 작을 때까지 반복
      int first = minusq.remove();
      int second = minusq.remove();
      sum = sum + first * second;
    }
    if (!minusq.isEmpty()) { // 큐에 하나만 남아있으면 0이 존재하는지 체크
      if (zero == 0) { // 0이 없으면
        sum = sum + minusq.remove(); // 남아 있는 것을 sum에 더함
      } // 0이 있으면 결국 0을 더하는 것이므로 따로 처리 필요 X
    }

    // (4) 1 처리하기
    sum = sum + one;
    System.out.println(sum);    
  }
}

