import java.io.*;
import java.util.*;

class Main {  
  
  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int target = sc.nextInt();

    int[] A = new int[N];

    int start = 0;
    int end = 0;
    for (int i = 0; i < N; i++) {
      A[i] = sc.nextInt();
      // start : 최대 길이의 레슨
      if (A[i] > start)
        start = A[i];
      // end : 모든 레슨 길이의 합
      end += A[i];
    }

    // 이진 탐색 수행
    while(start <= end) {
      int mid = (start + end) / 2;
      
      // 레슨 합
      int sum = 0;
      // 현재 사용한 블루레이 개수
      int count = 0;
      
      // mid값(현재 블루레이 크기)으로 모든 레슨을 저장할 수 있는지 확인**
      for (int i = 0; i < N; i++) {
        if (sum + A[i] > mid) {
          count++; // 블루레이 개수 추가
          sum = 0;
        }
        sum += A[i];
      }
      // 탐색 후 sum이 0이 아니면, 나머지를 담을 블루레이가 1개 더 필요하므로 count++
      if (sum != 0) {
        count++;
      }

      // 블루레이 크기를 줄일지 늘릴지 결정
      if (count > target) {
         // 목표 개수보다 블루레이 수가 많으면 (= 중간 인덱스 값으로 모든 레슨 저장 불가능)
         // -> 블루레이 크기 증가 (start = mid + 1)
        start = mid + 1;
      } else {
         // 목표 개수보다 블루레이 수가 적으면 (= 중간 인덱스 값으로 모든 레슨 저장 가능)
         // -> 블루레이 크기 감소 (end = mid - 1)
        end = mid - 1;
      }        
    }
    
    // while문이 종료된 뒤, 시작 인덱스 출력 
    // ('최솟값'을 구하는 것이므로 가장 작은 시작 인덱스 출력)
    // equal(==)값을 출력하는 것은 의미가 없음(=> '최솟값'이 아니더라도 equal값에 포함될 수 있기 때문!)
    System.out.println(start);
    
  }

}
