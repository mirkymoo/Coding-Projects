# Design a program that will use a pair of nested loop to read the company's sales amounts
# Company has 3 departments: 1. Dept X 2. Dept Y 3. Dept Z. 
# Design a program that will read as input each department's sales for each quarter of the year, 
# and display the result for all divisions. 
# Use a two dimensional array that will have 3 rows and 4 columns and show how the data will be organized.


curr_col_let = "X"
array = [[0]*4 for _ in range(3)]
for dept in range(3):
    for quarter in range(4):
        array[dept][quarter] = float(input(f"Enter the sales for Dept {curr_col_let}, Quarter {quarter+1}: "))
    curr_col_let = chr(ord(curr_col_let) + 1)


curr_col_let = "X"
print("Department\tQ1\t\tQ2\t\tQ3\t\tQ4")
for _ in array:
    print(curr_col_let, "\t\t", end=" ")
    curr_col_let = chr(ord(curr_col_let) + 1)
    for i in _:
        print(i,end="\t\t")
    print()