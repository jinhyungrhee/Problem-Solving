import java.util.*;

class Solution {
    // BFS Queue에서 사용할 Point 클래스 정의 - (3)
    class Point {
        int row, col, dist;
        
        // 값을 편하게 할당하기 위해서 생성자 정의
        Point(int r, int c, int d) {
            this.row = r;
            this.col = c;
            this.dist = d;
        }
    }
    
    // 상하좌우 이동을 위한 delta 배열 - (4)
    int[][] D = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
    
    // bfs함수 정의 - (5)
    boolean bfs(String[] place, int row, int col) { // 대기실에 대한 정보와 대기자의 위치 정보 입력으로 주어짐 -> 5개 짜리 String 5개가 주어짐 (5X5)
        boolean[][] visited = new boolean[5][5]; // Java는 new로 생성하면 자동으로 0이나 false로 zero initializtion됨!
        
        Queue<Point> q = new LinkedList<>();
        // 시작 위치를 queue에 집어넣기 전에 visited 마킹
        visited[row][col] = true;
        // queue에 enqeue
        q.add(new Point(row, col, 0)); // 시작위치의 거리(dist)는 0
        
        while(!q.isEmpty()) {
            Point curr = q.poll(); // remove()도 가능
            
            // 지금 위치에서 거리가 2를 초과했으면 skip
            if (curr.dist > 2) continue;
            // 거리가 2이하면 다른 응시자 확인 (시작위치가 아니고 다른 응시자가 있으면)
            if (curr.dist != 0 && place[curr.row].charAt(curr.col) == 'P') {
                return false; // 거리가 2이하면서 다른 응시자 존재(false)
            }
            
            for (int i = 0; i < 4; i++) {
                int nr = D[i][0] + curr.row;
                int nc = D[i][1] + curr.col;
                // 대기실의 좌표값을 벗어나는지 체크
                if (nr < 0 || nr > 4 || nc < 0 || nc > 4) continue;
                // 이미 방문한 적 있는지 체크
                if (visited[nr][nc]) continue;
                // 파티션이 존재하는지 체크
                if (place[nr].charAt(nc) == 'X') continue;
                
                visited[nr][nc] = true;
                q.add(new Point(nr, nc, curr.dist + 1));
            }
        }
        // 만약 거리 2이내에서 다른 응시자를 만나지 않으면 while문이 끝남
        // 즉, 거리두기가 지켜짐!
        return true;
        
    }
    
    boolean check(String[] place) { // 대기실에 대한 정보 입력으로 주어짐 -> 5개 짜리 String 5개가 주어짐 (5X5)
        
        // P 위치 찾기
        for (int r = 0; r < 5; r++) {
            for (int c = 0; c < 5; c++) {
                if (place[r].charAt(c) == 'P') {
                    // 해당 위치에 bfs() 호출 - (2)
                    // 거리두기가 지켜지지 않았다면 false 반환
                    if (bfs(place, r, c) == false) return false;
                }
            }
        }
        // 모든 경우 문제가 없다면 거리두기 지켰으므로 true 반환
        return true;
    
    }
    
    public int[] solution(String[][] places) {
        int[] answer = new int[5]; // 반환해야 하는 Array의 크기는 5로 정해져있음
        
        for (int i = 0; i < 5; i++) {
            if (check(places[i])) { // check()가 true를 리턴하면 거리두기 지켜짐 - (1)
                answer[i] = 1;
            } else { // check()가 false를 리턴하면 지켜지지 않음
                answer[i] = 0;
            }
        }
        
        
        return answer;
    }
}

/*
입력
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

출력
result = [1, 0, 1, 1, 1]
*/

// ezsw님 모범답안