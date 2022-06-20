import java.io.*;
import java.util.*;

class Main {   
  // 6가지 이동 케이스(경우)를 표현하기 위한 배열 **
  static int[] Sender = {0, 0, 1, 1, 2, 2};
  static int[] Receiver = {1, 2, 0, 2, 0, 1};
  // 방문 여부 체크 -> A,B 무게만 있으면 C의 무게가 고정되므로 2개만 체크 **
  static boolean[][] visited;
  // 정답 배열
  static boolean[] answer;
  // A,B,C 양동이 부피 저장 배열
  static int[] now;
  
  public static void main(String[] args) throws IOException {

    Scanner sc = new Scanner(System.in);

    // A, B, C 양동이 부피 저장
    now = new int[3];
    now[0] = sc.nextInt();
    now[1] = sc.nextInt();
    now[2] = sc.nextInt();

    // 최대 크기로 방문 배열, 정답 배열 초기화 (false)
    visited = new boolean[201][201];
    answer = new boolean[201];

    // BFS 수행
    BFS();

    // 결과 출력
    for (int i = 0; i < answer.length; i++) {
      if (answer[i]) 
        System.out.print(i + " ");
    }
  }

  public static void BFS() {
    Queue<AB> q = new LinkedList<>();
    q.add(new AB(0, 0)); // A B 초기화
    visited[0][0] = true;
    // 초기 조건(0, 0, C 양동이 full) 경우 방문 체크
    answer[now[2]] = true;

    while(!q.isEmpty()) {
      AB p = q.poll();
      int A = p.A;
      int B = p.B;
      int C = now[2] - A - B;
      // 6가지 경우(3P2)에 대해 탐색
      for (int i = 0; i < 6; i++) {
        // 새로운 배열(next)에서 물 주고받기 ***
        int[] next = {A, B, C};
        next[Receiver[i]] += next[Sender[i]]; // 물 보내기
        next[Sender[i]] = 0; // 보낸 양동이 물 비우기

        // 보냈는데 물이 넘치는 경우 ***
        if (next[Receiver[i]] > now[Receiver[i]]) {
          // 초과하는 만큼 Sender 양동이에 다시 담음
          next[Sender[i]] = next[Receiver[i]] - now[Receiver[i]];
          // 초과한 양동이는 최대 물양으로 update
          next[Receiver[i]] = now[Receiver[i]];
        }

        // A, B의 물 양을 이용하여 방문 배열 체크 ***
        // 주고 받은 결과(A,B : next[0], next[1])가 처음 확인하는 경우라면
        if (!visited[next[0]][next[1]]) {
          visited[next[0]][next[1]] = true;
          q.add(new AB(next[0], next[1]));
          // 정답 조건(A == 0)일 때의 C값을 정답 배열에 저장
          if(next[0] == 0) {
            answer[next[2]] = true;
          }
        }
      }      
    }
    
  }
}

class AB {
  int A;
  int B;

  public AB(int A, int B) {
    this.A = A;
    this.B = B;
  }
}