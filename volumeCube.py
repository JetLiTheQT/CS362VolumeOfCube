def volume(a,b,c):
    if((type(a) == str) or (type(b) == str) or (type(c) == str)):
        return "Invalid Input"
    if((a<= 0) or (b<=0) or (c <=0 )) :
        return "Invalid Input"
    else:
        return a*b*c

print(volume(-1,2,-3))