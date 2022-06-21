import java.util.*;
import java.io.*;

class Main {

    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()); // br.readLine()을 사용하려면 throws IOException 명시 필요!
        int N = Integer .parseInt(st.nextToken());

        // 이차원 ArrayLIst - 방법1
        // ArrayList<ArrayList<Integer>> A = new ArrayList<>();
        // for (int i = 0; i < N; i++) {
        //      A.add(new ArrayList<>());
        // }

        // ArrayLIst 배열 - 방법2
        ArrayList<Integer>[] A = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            A[i] = new ArrayList<Integer>();
        }

        // 진입 차수 배열
        int[] indegree = new int[N + 1];
        // 각 건물 '자체(개별)' 건설 시간 배열
        int[] build = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            build[i] = Integer.parseInt(st.nextToken());
            while (true) {
                int preTemp = Integer.parseInt(st.nextToken());
                if (preTemp == -1) break;
                A[preTemp].add(i); // preTemp -> i (preTemp 먼저 짓고 그 다음 i를 지어야 함)
                indegree[i]++; // 진입 차수 증가
            }
        }

        // *** 위상 정렬 수행 ***
        // 위상 정렬 배열(Queue)에 진입차수 0인 노드 저장
        Queue<Integer> q = new LinkedList<>();
        // 각 건물 '총(전체)' 건설 시간 배열
        int[] result = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                q.add(i);
            }
        }
        // 선택된 노드(=진입차수 0 노드)와 연결된 모든 노드 차수 1 감소
        while(!q.isEmpty()) {
            int now = q.poll();
            for (int next : A[now]) {
                indegree[next]--;
                // ** 각 건물 '총(전체)' 건설 시간 갱신 ***
                // 각 건물을 짓는 데 걸리는 '최대 시간'을 업데이트
                // max(현재 노드에 저장된 최대 시간, 이전 노드에 저장된 최대 시간 + 현재 노드의 생산 시간)
                result[next] = Math.max(result[next], result[now] + build[now]);

                // Q. 만약 현재 노드에 저장된 시간과 max()로 비교를 하지 않는다면?
                //result[next] = result[now] + build[now];
                // A. max()로 비교한 경우와 결과는 동일함 (10 20 14 18 17)
                // 왜 그럴까....? 그러면 굳이 왜 max()로 비교해야 하는 것일까?

                if (indegree[next] == 0) {
                    q.add(next);
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            System.out.println(result[i] + build[i]);
        }
    }
}