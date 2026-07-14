def isPrime(num):
	isPrime = False;
	if(num == 1):
		return isPrime;
	if(num == 2 or num == 3 or num == 5 or num == 7 or num == 11):
		isPrime = True;
		return isPrime;
			
	if(num % 11 != 0 and num % 7 != 0 and num % 5 != 0 and num % 3 != 0 and num % 2 != 0 ):
		isPrime = True;
		
	counter = 0;
	for i in range(1, num + 1):
		if(num % i == 0):
			counter = counter + 1;
		if(counter > 2 ):
			isPrime = False;
			break;
	return isPrime;

sum = 2;
for i in range(3, 2*1000*1000, 2):
	if(isPrime(i)):
		sum = sum + i;
print(sum);