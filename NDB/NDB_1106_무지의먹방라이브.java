public class MukbangLive {

    public static void main(String[] args) {

        int[] food_items = {3, 1, 2};
        long k = 5;

        int n = food_items.length;
        int last_idx = 0;

        int idx = 0;
        while (idx <= k) {
            if (food_items[idx % n] != 0) {
                food_items[idx % n] -= 1;
                last_idx = idx % n;
            }
            idx += 1;
        }

        if (food_items[(last_idx + 1) % n] != 0) {
//            System.out.println(food_items[(last_idx + 1) % n]);
            System.out.println((last_idx + 1) % n + 1); // 번호 출력
        } else {
            System.out.println(-1);
        }

        System.out.println((last_idx + 1) % n);
        for (int i= 0 ; i < n; i++) {
            System.out.print(food_items[i] + " ");
        }
    }
}


// 6.7/100