import java.util.*;
class Solution {
    
    class Food {
        int time;
        int idx;
        Food(int t, int i) {
            time = t;
            idx = i;
        }
    };
    // 시간 순서대로 정렬하기 위해 Comparator 구현 필요
    Comparator<Food> CompTime = new Comparator<Food>() {
        public int compare(Food a, Food b) {
            return a.time - b.time; // 시간 순서대로 오름차순으로 정렬
        }
    };
    
    // 음식 순서대로 정렬하기 위해 Comparator 구현 필요
    Comparator<Food> CompIdx = new Comparator<Food>() {
        public int compare(Food a, Food b) {
            return a.idx - b.idx; // 음식 순서대로 오름차순으로 정렬
        }
    };
    
    public int solution(int[] food_times, long k) {
        int answer = 0;
        List<Food> foods = new LinkedList<Food>();
        int n = food_times.length;
        for (int i = 0; i < n ; i++) {
            foods.add(new Food(food_times[i], i + 1)); // 음식 순서는 1부터 시작
        }
        
        foods.sort(CompTime); // '시간' 기준으로 오름차순 정렬
        
        int pretime = 0; // diff를 구하기 위한 이전시간
        int i = 0; // 몇 번째 처리중인지 체크하기 위한 인덱스
        
        for (Food f : foods ) { // for-each 문으로 순회
            long diff = f.time - pretime;
            if (diff != 0) {
                long spend = diff * n; // 쓸 수 있는 시간 (diff * 남아있는 음식 수)
                if (spend <= k) {
                    k -= spend;
                    pretime = f.time; // 현재 시간으로 pretime 갱신
                } else {
                    // 순회를 중단하고 답 구하기
                    k %= n;
                    // 남아있는 음식들을 원래 음식 순서대로 정렬(CompIdx 사용)
                    foods.subList(i, food_times.length).sort(CompIdx); // 현재 남아있는 음식부터 끝까지 잘라내기 + 정렬
                    return foods.get(i + (int)k).idx; // 현재 위치에서 k만큼 더해서 간 뒤의 idx 리턴
                }
            }
            ++i; // 인덱스 1씩 증가
            --n; // 남아있는 음식 하나씩 감소
        }
        
        // 만약 시간이 충분해서 다 먹었을 경우(남은 음식이 없는 경우)
        return -1;
    }
}

// 유튜버 ezsw님 코드 모범답안