def calcFibo(num):
	if(num > 2):
		return calcFibo(num - 1) + calcFibo(num - 2)
	return num;

def isEven(num):
	if(num % 2 == 0):
		return True;
	else:
		return False;
i = 1;
fiboSum = 0;
while(fiboSum <= 4000000):
	if(isEven(calcFibo(i))):
		fiboSum = fiboSum + calcFibo(i);
	i += 1;

print(fiboSum);
