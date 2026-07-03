def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
number = 1;
avalCount = 0;
# return;
while(True):
    if(is_prime(number)):
        print(number);
        avalCount = avalCount + 1;
    if(avalCount == 10001):
        break;
    number = number + 1;
