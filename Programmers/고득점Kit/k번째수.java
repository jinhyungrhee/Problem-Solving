import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int idx = 0; idx < commands.length; idx++) {
            int i = commands[idx][0] - 1;
            int j = commands[idx][1];
            int k = commands[idx][2] - 1; 
            int[] newArr = Arrays.copyOfRange(array, i, j);
            //System.out.println(newArr);
            Arrays.sort(newArr);
            answer[idx] = newArr[k];
        }
        
        return answer;
    }
}

/*
import java.util.Arrays;
[배열 복사] : Arrays.copyOfRange(arr, startIndex, endIndex+1);
 */