import java.util.*;
public class explorerGuild {

    public static int n;
//    public static int[] Arr = new int[100000];
    public static ArrayList<Integer> arrayList = new ArrayList<>(); // 가변길이 리스트

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

//        int n = sc.nextInt();
        n = sc.nextInt();

        for (int i = 0; i < n; i++) {
//            Arr[i] = sc.nextInt();
            arrayList.add(sc.nextInt());
        }

//        Arrays.sort(Arr);
        Collections.sort(arrayList);

        int totalGroup = 0; // 총 그룹수
        int gMember = 0; // 현재 그룹에 포함된 모험가의 수
        for (int i = 0; i < n; i++) { // 공포도 낮은 것부터 하나씩 확인
            gMember += 1; // 현재 그룹에 해당 모험가 포함시킴
            if (gMember >= arrayList.get(i)) { // 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이면 그룹 결성
                totalGroup += 1; // 총 그룹 수 증가
                gMember = 0; // 현재 그룹에 포함된 모험가의 수 초기화
            }
            
        }

        System.out.println(totalGroup);

    }
}