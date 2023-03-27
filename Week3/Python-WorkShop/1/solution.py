def main(a, b, c):
    if  not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        return "err"
    elif c == 0 or (a == 0 and b == 0):
        return "err"
    else:
        result = (a + b) / c
        return result

    