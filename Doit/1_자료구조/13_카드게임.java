import java.util.*;

class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();

    Queue<Integer> myQueue = new LinkedList<>();

    for (int i = 1; i <= N; i++) {
      myQueue.add(i);
    }

    while(myQueue.size() > 1) { // 한 장이 남을 때까지 반복
      // 맨 위의 카드 버림
      myQueue.poll();
      // 맨 위의 카드를 가장 아래의 카드 밑으로 이동
      myQueue.add(myQueue.poll());
    }

    // 마지막 남은 카드 출력
    System.out.println(myQueue.poll());
  }
}