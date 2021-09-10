def swap_case(s):
    result = ""
    for a in s:
        if(a.isupper()):
            result += (a.lower())
        elif(a.islower()):
            result += (a.upper())
        else:
            result += a  
    return result
s = input()
result = swap_case(s)
print(result)
    
