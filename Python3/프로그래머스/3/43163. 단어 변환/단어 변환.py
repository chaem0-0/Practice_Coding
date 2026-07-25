from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    
    q = deque([(begin, 0)])

    while q:
        word, answer = q.popleft()
        
        if word == target:
            return answer
        
        for i in range(len(words)):
            if not visited[i] and check(word, words[i]):
                visited[i] = True
                q.append((words[i], answer + 1))   
    
    return answer

def check(word1, word2):
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
            
    return diff == 1