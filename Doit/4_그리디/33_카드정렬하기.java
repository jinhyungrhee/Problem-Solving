import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();

    PriorityQueue<Integer> pq = new PriorityQueue<>(); // default로 오름차순 정렬?

    for (int i = 0; i < N; i++) {
      pq.add(sc.nextInt());
    }

    int result = 0;
    int compare = 0;
    while(pq.size() != 1) {
      int first = pq.poll();
      int second = pq.poll();
      result = first + second;
      compare += result; // 비교횟수의 합 기록
      pq.add(result);
    }
    

    System.out.println(compare);
    
  }
}

