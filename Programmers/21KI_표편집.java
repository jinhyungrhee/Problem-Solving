import java.util.*;

class Solution {
    class Node {
        boolean removed; // 삭제 유무
        Node prev; // 이전 노드 가리키는 링크
        Node next; // 다음 노드 가리키는 링크
    }
    
    Node[] nodeArr = new Node[1000000]; // 최대 입력 개수
    // Class(Node)와 Array(nodeArray) 모두 reference Type이므로 한번에 백만개의 Node가 생성되지 않음
    // Node 객체를 가리킬 수 있는 reference변수만 백만개 생성됨!
    
    public String solution(int n, int k, String[] cmd) {
        // 객체 n개만 만들기
        for (int i = 0; i < n; i++) {
            nodeArr[i] = new Node(); //i번 인덱스에 있는 refernce변수 값이 생성된 노드 객체를 가리키게 됨!
            // new로 생성하게 되면 zero initialization됨 (removed = false, prev = null, next = null)
        }
        // 초기화 (링크 연결)
        for (int i = 1; i < n; i++) {
            nodeArr[i - 1].next = nodeArr[i]; // 처음 nodeArr[i-1].prev는 이미 null 
            nodeArr[i].prev = nodeArr[i - 1]; // 마지막 nodeArr[i].next는 이미 null
        }
        
        Node curr = nodeArr[k]; // curr은 k번째 노드를 가리킴
        
        // 복원을 위한 스택
        Stack<Node> mystack = new Stack<>();
        
        for (String str : cmd) {
            if (str.charAt(0) == 'U') {
                // int x = str.split(" ")[1]
                int x = Integer.parseInt(str.substring(2)); // 2번 인덱스부터 끝까지
                // x만큼 prev 링크 타고 올라감
                for (int i = 0; i < x; i++) {
                    curr = curr.prev;
                }
            } else if (str.charAt(0) == 'D') {
                int x = Integer.parseInt(str.substring(2)); // 2번 인덱스부터 끝까지
                // x만큼 next 링크 타고 내려감
                for (int i = 0; i < x; i++) {
                    curr = curr.next;
                }
            } else if (str.charAt(0) == 'C') { // 삭제
                mystack.push(curr); // 스택 저장
                curr.removed = true; // 삭제 표시
                
                Node up = curr.prev; // 현재 행이 첫번째 행이면 prev는 null임 -> 체크!
                Node down = curr.next; // 현재 행이 마지막 행이면 next는 null임 -> 체크!
                
                // null이 아닐 때만 건너뛰어서 가리킴
                if (up != null)
                    up.next = down;
                if (down != null) {
                    down.prev = up;
                    curr = down; // 선택된 행을 바로 아래 행으로 옮김
                } else {
                    // 만약 마지막 행이었으면
                    curr = up; // 선택된 행을 바로 윗 행으로 옮김
                }
            } else { // Z - 복구 (curr값 바꾸지 않음!)
                Node node = mystack.pop();
                node.removed = false;
                // 링크 복원
                Node up = node.prev;
                Node down = node.next;
                // 복원되는 노드가 첫번째 or 마지막인지 체크
                if (up != null) 
                    up.next = node; // 지금 보고있는 노드를 가리키도록 변경
                if (down != null)
                    down.prev = node;
            }
        }
            
        // array를 순회하면서 removed값만 체크!
        
        // 하나하나 append하기 때문에 String보다는 StringBuilder 사용!
        // String(Immutable) : 더할 때마다(concat) 매번 새로운 객체 생성됨
        // StringBuilder(mutable) : 더할 때마다(append) 새로운 객체 생성되지 않음 (객체의 값만 변경)
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (nodeArr[i].removed)
                answer.append('X');
            else
                answer.append('O');
        }
        return answer.toString(); // StringBuilder에서 String으로 변경
    }
}

/*
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
result = "OOOOXOOO"
 */

/*
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
result = "OOXOXOOO"
 */

// ezsw님 모범답안 참고