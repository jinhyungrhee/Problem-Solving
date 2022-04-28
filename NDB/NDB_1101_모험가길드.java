import java.util.*;

class Main{
  static int n;
  static ArrayList<Integer> arrayList = new ArrayList<>();
  
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    n = sc.nextInt();

    for (int i = 0; i < n; i++) {
      arrayList.add(sc.nextInt());
    }

    Collections.sort(arrayList);

    int gNum = 0;
    int mNum = 0;
    for (int i = 0; i < n; i++) {
      mNum += 1;
      if (arrayList.get(i) <= mNum) {
        mNum = 0; // 멤버 수 초기화
        gNum += 1; // 그룹 하나 결성
      }
    }
    System.out.println(gNum);
  }
}