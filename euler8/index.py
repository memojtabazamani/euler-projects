number = "7316717";
number_len = len(number);
number_div_group = 3;


number_home = 0;
zarb = [];
while(True):
	number_grouped = number[number_home:number_home + number_div_group]
	if(len(number_grouped) < number_div_group):
		break;
	print(number_grouped);
	number_home = number_home + 1;