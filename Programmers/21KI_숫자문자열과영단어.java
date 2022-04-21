class Solution {
    String[] Word = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    public int solution(String s) {
        // java에서 String은 immutable 타입 -> concat()을 하면 매번 새로운 String 객체가 생성됨
        // 따라서 mutable 클래스인 StringBuilder 사용!
        StringBuilder sb = new StringBuilder();
        
        for (int pos = 0; pos < s.length(); ) {
            if (s.charAt(pos) >= '0' && s.charAt(pos) <= '9') { // 숫자인 경우
                sb.append(s.charAt(pos++));
            } else { // 영단어인 경우
                for (int i = 0; i < 10; i++) {
                    if (s.startsWith(Word[i], pos)) { // 현재 위치에서 Word[i] 단어가 시작하는지 확인
                        sb.append((char)('0' + i));
                        pos += Word[i].length(); // 단어 길이에 맞게 위치 재조정
                        break; // 단어 하나만 찾으면 되므로 for문 탈출
                    }
            
                }

            }
            
        }
        
        int answer = Integer.parseInt(sb.toString());
        return answer;
    }
}