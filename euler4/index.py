def isPald(num):
	digits = [int(d) for d in str(num)]
	isP = True;
	for i in range(len(digits)):
		if(digits[i] != digits[len(digits) - i - 1]):
			isP = False;
	return isP;

i = 100;
j = 100;
number = 0;
paldNumbers = [];
while(i <= 999):
	while (j <= 999):
		number = i * j;
		if(isPald(number)):
			if number not in paldNumbers:
				paldNumbers.append(number)
		j+=1;
	j = 100;
	i+=1;
paldNumbers = sorted(paldNumbers);
print(paldNumbers[len(paldNumbers) - 1]);