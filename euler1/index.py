def myFunc(i):
	if i%3==0 or i%5==0:
		return True;
	else:
		return False;
sum = 0;
for i in range(1, 1000):
	if(myFunc(i)):
		sum += i;

print(sum)