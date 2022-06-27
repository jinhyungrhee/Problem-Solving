def solution(s):
    answer = len(s) # 초기 정답값(압축 처리가 하나도 되지 않은 문자열의 길이)
    
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step] # 이전 문자열
        count = 1 

        # 부분 문자열을 step 크기만큼 증가(s[i:i+step])시키면서 이전 문자열(s[0:step])과 비교 **
        for j in range(step, len(s), step):

            # 현재 부분 문자열이 이전 상태와 동일하다면 압축 횟수 증가 **
            if prev == s[j:j+step]:
                count += 1
            # 현재 부분 문자열에 다른 문자가 등장하여 이전 문자열과 다르다면(= 더이상 압축 불가)
            else: 
                # 지금까지 압축된 것들 반영함
                compressed += str(count) + prev if count >=2 else prev
                prev = s[j:j+step] # 이전 문자열을 현재 부분 문자열로 갱신
                count = 1 # 압축 개수 초기화
        
        # 남아 있는 문자열에 대해서 처리
        # 만약 j-for문이 if문에서 끝날 경우, 압축된 것이 반영되지 못한 상태로 종료됨
        # 따라서 지금까지 압축된 것들을 반영하는 과정이 한 번 더 필요
        compressed += str(count) + prev if count >= 2 else prev

        # j-for문이 끝날 때마다 만들어지는 압축 문자열들을 비교하여 가장 짧은 것으로 갱신함
        answer = min(answer, len(compressed))
        
    return answer