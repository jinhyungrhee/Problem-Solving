class Solution {
    
    static int count;
    
    public int solution(int[] numbers, int target) {
        
        count = 0;
        
        DFS(numbers, target, 0, 0);
        
        return count;
    
    }
    
    public int DFS(int[] numbers, int target, int index, int sum) {
        
        if (index == numbers.length && sum == target) {
            count++;
            return 0;
        }
        
        if (index == numbers.length) {
            return 0;
        }
        
        DFS(numbers, target, index + 1, sum + numbers[index]);
        DFS(numbers, target, index + 1, sum - numbers[index]);
        
        return 0;
        
    }
               
}