def calcFibo(num):
	if(num > 2):
		return calcFibo(num - 1) + calcFibo(num - 2)
	return num;
for i in range(1, 11):
	if(i == 1 or i == 2):
		continue;
	else:
		print("fibo of ", i, "is ", calcFibo(i))
	
	
