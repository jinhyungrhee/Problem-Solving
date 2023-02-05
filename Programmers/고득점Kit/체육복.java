class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int[] student = new int[n];
        
        for (int l : lost) {
            student[l-1]--;
        }
        for (int r : reserve) {
            student[r-1]++;
        }
        
        //System.out.println(Arrays.toString(student));
        
        // student 배열을 선행탐색하면서 -1일때 양 옆에 1이 있는지 확인
        for (int i = 0; i < student.length; i++) {
            if (student[i] == -1) {
                if (i-1 >= 0 && student[i-1] == 1) {
                    student[i]++;
                    student[i-1]--;
                }
                else if (i+1 < n && student[i+1] == 1) { // 주의!) 예외조건을 먼저 판단해야 함
                    student[i]++;
                    student[i+1]--;
                }
                else {
                    answer--;
                }
            }
        }
        
        //System.out.println(Arrays.toString(student));
        //System.out.println(answer);
        
        return answer;
    }
}