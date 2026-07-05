def isNature(num):
    return num > 0 and isinstance(num, int)

a = b = c = counter = 0;
a = 1;
b = 2;
c = 3;
br = True;
while(True):
    counter = counter + 1;
    fis = a**2 + b**2;
    if(fis == c**2):
        if(a + b + c == 1000):
            print(a,b,c);
            break;
    else:
        if(b + 1 <= c):
            b = b + 1;
        else:
            a = a + 1;
            b = a + 1;
    c = abs(1000 - a - b);