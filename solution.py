def accum(s):

    answer = ""

    for i, c in enumerate(s):
        if i == 0:
            answer += c.upper() + '-'
        elif i < len(s)-1:
            answer += c.upper() + c.lower()*i + '-'
        else:
            answer += c.upper() + c.lower()*i
            
         
    return answer
