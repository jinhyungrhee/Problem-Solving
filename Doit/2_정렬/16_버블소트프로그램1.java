import java.io.*;
import java.util.*;

class Main{
  
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    // 저장 배열 선언
    mData[] A = new mData[N];

    for (int i = 0; i < N; i++) {
      A[i] = new mData(Integer.parseInt(br.readLine()), i);
    }

    // 정렬 전 index - 노드에 저장됨
    // 10(0), 1(1), 5(2), 2(3), 3(4)
    
    Arrays.sort(A); // NlogN

    // 정렬 후 index - 배열에 저장됨
    // 1(0), 2(1), 3(2), 5(3), 10(4)

    // 정렬 전 index와 정렬 후 index 차이의 최댓값 구하기 **
    int Max = 0;    

    for (int i = 0; i < N; i++) {
      if (Max < A[i].index - i)
        Max = A[i].index - i;
    }
    
    System.out.println(Max + 1); // swap이 일어나지 않는 반복문 횟수 추가
    
  }
}

class mData implements Comparable<mData> {
  int value;
  int index;

  public mData(int value, int index) {
    this.value = value;
    this.index = index;
  }

  @Override
  public int compareTo(mData o) { // value 기준 오름차순 정렬
    return this.value - o.value;
  }
}