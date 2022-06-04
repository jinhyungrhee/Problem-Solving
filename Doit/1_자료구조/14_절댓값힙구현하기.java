import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());

    // 절대값 작은 순으로 정렬되는 우선순위 큐 선언 **
    PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> { // 람다식 사용
      int first_abs = Math.abs(o1);
      int second_abs = Math.abs(o2);
      if (first_abs == second_abs)
        return o1 > o2 ? 1 : -1; // 절대값이 같으면 음수 우선 정렬
      else
        return first_abs - second_abs; // 절대값을 기준으로 정렬
    });

    // 들어온 요청에 따라 분류
    for (int i = 0; i < N; i++) {
      int request = Integer.parseInt(br.readLine());
      // 요청이 0일 때, 가장 작은 값 출력
      if (request == 0) {
        if (pq.isEmpty()) { // 큐에 아무 값도 없으면 0 출력
          System.out.println("0");
        } else {
          System.out.println(pq.poll());
        }
      } 
      // 요청이 0이 아닐 때, 큐에 값 추가
      else {
        pq.add(request);
      }      
    }
    
  }
}