def solution(my_string):
    answer = []
    for i in range(0,len(my_string)):
        if my_string[i].isnumeric():
            answer.append(int(my_string[i]))
            
    answer.sort()
    return answer