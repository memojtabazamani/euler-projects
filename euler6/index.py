maxNumber = 101;
minNumber = 1;
calcOfSumSquares = 0;

for i in range(minNumber, maxNumber):
    calcOfSumSquares = calcOfSumSquares + i**2;

print(calcOfSumSquares);

print('*************');

calcofSquareOfTheSum = 0;
for i in range(minNumber, maxNumber):
    calcofSquareOfTheSum = calcofSquareOfTheSum + i;

calcofSquareOfTheSum = calcofSquareOfTheSum**2;

print(calcofSquareOfTheSum);

print('*************');

diff = calcofSquareOfTheSum - calcOfSumSquares;

print("The diffrent of ",calcOfSumSquares, " And ", calcofSquareOfTheSum, " is = ",  diff);
