import java.util.*;

class Main{

  static ArrayList<Integer> arrayList = new ArrayList<>();
  
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String str = sc.nextLine();
    
    for (int i = 0; i < str.length(); i++) {
      arrayList.add(str.charAt(i) - '0'); // char to int
    }

    Collections.sort(arrayList);

    int result = arrayList.get(0);
    for (int i = 1; i < arrayList.size(); i++) {
      if (arrayList.get(i - 1) == 0) {
        result += arrayList.get(i);
      } else {
        result *= arrayList.get(i);
      }
    }

    System.out.println(result);
  }
}

// 오답
// 1) 굳이 ArrayList 쓰지 않아도 됨
// 2) S의 최대 길이가 20이므로 결과값의 자료형은 long
// 3) 0과 1 모두 고려해야 함!