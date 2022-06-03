import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // 출력을 버퍼에 넣고 한 번에 출력하기 위해 BufferedWriter 사용
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken()); // 데이터 개수
    int L = Integer.parseInt(st.nextToken()); // 윈도우 사이즈

    Deque<Node> mydeque = new LinkedList<>(); // 데이터를 담을 덱 (덱을 이용한 정렬효과)

    st = new StringTokenizer(br.readLine());
    // 모든 인덱스에 대해 반복
    for (int i = 0; i < N; i++) {
      int now = Integer.parseInt(st.nextToken());

      // 새로운 값이 들어올 때마다 정렬 대신, 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도 줄임**
      while (!mydeque.isEmpty() && mydeque.getLast().value > now) {
        mydeque.removeLast();
      }

      mydeque.addLast(new Node(now, i)); // 값-인덱스 순서

      // 범위에서 벗어난 값은 덱에서 제거
      if (mydeque.getFirst().index <= i - L) {
        mydeque.removeFirst();
      }
      bw.write(mydeque.getFirst().value + " "); // 일단 버퍼에 저장하고 나중에 한 번에 출력**
    }
    
    // 끝나면 버퍼 비우고 닫기
    bw.flush();
    bw.close();
    
   }

  static class Node {
    public int value;
    public int index;

    Node(int value, int index) {
      this.value = value;
      this.index = index;
    }
  }
}