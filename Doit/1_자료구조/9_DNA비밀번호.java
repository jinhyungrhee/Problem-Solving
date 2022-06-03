import java.io.*;
import java.util.*;

class Main{
  // 전역 변수로 정의
  static int checkArr[]; // 비밀번호 체크 배열
  static int myArr[]; // 현재 상태 배열
  static int checkSecret; // 비밀번호 유효성 검사 변수
  
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int S = Integer.parseInt(st.nextToken()); // 문자열 크기
    int P = Integer.parseInt(st.nextToken()); // 부분 문자열 크기

    int result = 0;
    char[] A = new char[S]; // 문자열 데이터    
    checkArr = new int[4];
    // 변수 선언
    myArr = new int[4];
    checkSecret = 0;

    A = br.readLine().toCharArray();
    // String A = br.readLine();
    // char[] arrA = A.toCharArray();
    st = new StringTokenizer(br.readLine());

    // checkArr 채우기
    for (int i = 0; i < 4; i++) {
      checkArr[i] = Integer.parseInt(st.nextToken());
      if (checkArr[i] == 0) checkSecret++; // ?
    }

    // 초기 P 부분 문자열 처리 부분
    for (int i = 0; i < P; i++) {
      Add(A[i]);
    }
    if (checkSecret == 4) result++;

    // 슬라이딩 윈도우 처리 부분 **
    for (int i = P; i < S; i++) {
      int j = i - P;
      Add(A[i]);
      Remove(A[j]);
      if (checkSecret == 4) result++;
    }

    System.out.println(result);
    br.close();
    
  }

  // 새로 들어온 문자를 처리하는 함수
  private static void Add(char c) {
    switch(c) {
    case 'A' :
      myArr[0]++;
      if (myArr[0] == checkArr[0]) checkSecret++;
      break;
    case 'C' :
      myArr[1]++;
      if (myArr[1] == checkArr[1]) checkSecret++;
      break;
    case 'G' :
      myArr[2]++;
      if (myArr[2] == checkArr[2]) checkSecret++;
      break;
    case 'T' :
      myArr[3]++;
      if (myArr[3] == checkArr[3]) checkSecret++;
      break;
    }
  }
  
  // 제거되는 문자를 처리하는 함수
  private static void Remove(char c) {
    switch(c) {
    case 'A' :
      if (myArr[0] == checkArr[0]) checkSecret--;
      myArr[0]--;
      break;
    case 'C' :
      if (myArr[1] == checkArr[1]) checkSecret--;
      myArr[1]--;
      break;
    case 'G' :
      if (myArr[2] == checkArr[2]) checkSecret--;
      myArr[2]--;
      break;
    case 'T' :
      if (myArr[3] == checkArr[3]) checkSecret--;
      myArr[3]--;
      break;
    }
  }
}