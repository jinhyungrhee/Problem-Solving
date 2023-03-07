import java.util.*;
class Solution {
    
    public int solution(int[] numbers, int target) {
        
        int count = 0;
        
        Queue<Node> queue = new LinkedList<>();
    
        // 양수에서 시작
        queue.add(new Node(numbers[0], 0));
        // 음수에서 시작
        queue.add(new Node(-1 * numbers[0], 0));
        
        while(!queue.isEmpty()) {
            
            Node now = queue.poll();
            if (now.index == numbers.length - 1) {
                if (now.sum == target) {
                    count++;
                }
                continue; // 다음 노드 poll()
            }
            
            int nextIndex = now.index + 1;
            if (nextIndex >= numbers.length) continue; // 범위 넘어감
            
            queue.add(new Node(now.sum + numbers[nextIndex], nextIndex));
            queue.add(new Node(now.sum - numbers[nextIndex], nextIndex));
            
        }
        
        //System.out.println(queue.peek().value);
        //System.out.println(queue.peek().index);

        return count;
    
    }
        
}
    
class Node {
    int sum;
    int index;
    
    public Node(int sum, int index) {
        this.sum = sum;
        this.index = index;
    }
}