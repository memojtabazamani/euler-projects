def isPald(num):
	digits = [int(d) for d in str(num)]
	isP = True;
	for i in range(len(digits)):
		if(digits[i] != digits[len(digits) - i - 1]):
			isP = False;
	print(isP);

isPald(101);
# i = 100;
# j = 100;
# number = 0;
# while(i <= 999):
	# while (j <= 999):
		# print("j is", j);
		# number = i * j;
		# j+=1;
	# print("i is", i);
	# i+=1;