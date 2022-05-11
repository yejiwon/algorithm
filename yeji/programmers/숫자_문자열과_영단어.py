def solution(s):
    keys = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for index in range(len(keys)):
        s = s.replace(keys[index], str(index))
        
    return int(s)