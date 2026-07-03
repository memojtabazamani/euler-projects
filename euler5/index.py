def multipleNumb(numb):
    for i in range(1,21):
        if(numb % i != 0):
            return False;
    return True;        

number = 20;

while(True):
    if(multipleNumb(number)):
        print(number);
        break;
    number = number + 1;