curr_col_let = "X"
array = [[0]*4 for _ in range(3)]
for dept in range(3):
    for quarter in range(4):
        array[dept][quarter] = float(input(f"Enter the sales for Dept {curr_col_let}, Quarter {quarter+1}: "))
    curr_col_let = chr(ord(curr_col_let) + 1)


curr_col_let = "X"
print("Department \tQ1\t\tQ2\t\tQ3\t\tQ4")
for _ in array:
    print(curr_col_let, "\t\t", end=" ")
    curr_col_let = chr(ord(curr_col_let) + 1)
    for i in _:
        print(i,end="\t\t")
    print()