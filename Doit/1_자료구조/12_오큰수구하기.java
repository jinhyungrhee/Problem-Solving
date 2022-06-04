import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    int[] A = new int[N]; // 수열 배열
    int[] ans = new int[N]; // 정답 배열

    // 수열 입력 받기
    String[] str = br.readLine().split(" ");
    for (int i = 0; i < N; i++) {
      A[i] = Integer.parseInt(str[i]);
    }

    // 인덱스를 저장하는 스택
    Stack<Integer> myStack = new Stack<>();
    // 비어있는 스택에 최초값(0번 인덱스)을 push해서 스택 초기화
    myStack.push(0); 
    
    for(int i = 1; i < N; i++) {
      // 스택이 비어있지 않고, 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
      while (!myStack.isEmpty() && A[i] > A[myStack.peek()]) {
        // 정답 배열에 오큰수를 현재 수열로 저장
        ans[myStack.pop()] = A[i];
      }
      myStack.push(i); // 신규 데이터 push
    }
    // 반복문을 다 돌고 나왔는데 스택이 비어 있지 않다면, 빌 때까지 수행
    while(!myStack.isEmpty()) {
      ans[myStack.pop()] = -1; // 스택에 쌓인 인덱스에 -1 넣음
    }
    // 버퍼에 저장하여 한꺼번에 출력
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    for (int i = 0; i < N; i++) {
      bw.write(ans[i] + " ");
    }
    bw.write("\n");
    bw.flush();
  }
}