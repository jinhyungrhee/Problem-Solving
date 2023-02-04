class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int maxVal1 = 0;
        int maxVal2 = 0;
        for (int i = 0; i < sizes.length; i++) { 
            
            int smaller = 1001;
            for (int j = 0; j < sizes[i].length; j++){
                // 가장 큰 수 구하기
                if (sizes[i][j] > maxVal1) {
                    maxVal1 = sizes[i][j];
                }
                
                // 가로, 세로 중 더 작은 수 구하기 (각 수는 1000을 넘지 않음)
                if (sizes[i][j] < smaller) {
                    smaller = sizes[i][j];
                }
            }
            
            // 더 작은 수중에서 가장 큰 수 구하기
            if (smaller > maxVal2) {
                maxVal2 = smaller;
            }
        }
        
        answer = maxVal1 * maxVal2;
        
        return answer;
    }
    
}