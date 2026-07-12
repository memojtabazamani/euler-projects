import math

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
];

# print(matrix[2][0:2]);
# print(matrix[0][0]);
# print(matrix[1][0]);
# print(matrix[2][0]);


index_i = 0
index_j = 0
col_numbers = 4;
spliter_num = 4;
numbers = [];
row = 0;
row_j = 0;
col = 0;
counter_number = 0;
while col < len(matrix) - 1:
    while row < col_numbers:
        while(counter_number < spliter_num):
            if(row_j >= col_numbers):
                break;
            numbers.append(matrix[row_j][col]);
            row_j = row_j + 1;
            
            counter_number = counter_number + 1;
        
        result = math.prod(numbers);
        numbers = [];
        # #row_j = 0;
        print(result)  
        # # if(row == spliter_num):
        # #     break;
        if(counter_number <= spliter_num):
            if(row_j == col_numbers):
                break;
            row_j = row_j - (spliter_num - 1);
            counter_number = 0;
    row =counter_number= row_j = 0;    
    col = col + 1;    
    


# for i in range(len(matrix) - 1):
#     for j in range(spliter_num):
#         if(j == spliter_num):
#             i = i + 1;
#         print(matrix[j][i]);
#         numbers.append(matrix[j][i]);



# while index_i < len(matrix):
#     print(matrix[index_i][index_j]);
#     index_i += 1
#     if index_i == 2:
#         index_j += 1
#         if index_j == 3:
#             break
#         index_i = 0
    
    




matrix[0][0]
matrix[1][0]
matrix[2][0]
matrix[3][0]

matrix[0][1]
matrix[1][1]
matrix[2][1]
matrix[3][1]

matrix[0][2]
matrix[1][2]
matrix[2][2]
matrix[3][2]



# print(matrix[0:2][0]);
# print(matrix[0]);