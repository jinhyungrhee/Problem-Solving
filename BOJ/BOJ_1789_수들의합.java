import java.util.*;

class Main{
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    long n = sc.nextLong();

    long sum = 0;
    int i = 0;
    while(true) {
      i++;
      sum += i;

      if (sum > n) {
        i--;
        break;
      } else if (sum == n) {
        break;
      }
    }    

    System.out.println(i);
  }
}