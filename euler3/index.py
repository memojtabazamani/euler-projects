def isAval(numb):
	if(numb > 1 ):	
		if( numb == 2 or ( numb % 1 == 0 or numb % numb == 0) and ( numb % 2 != 0 and numb % 3 != 0 )):
			return True;
		return False

counter = 1;
number = 600851475143;

while(True):
	if(isAval(counter)):
		if(number % counter == 0):
			number = number / counter;
			print(number);
	if(number == 1): break;
	counter+=1;