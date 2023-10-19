#prints 
#1A 1B 1C 
#2A 2B 2C 


num_rows = int(input())
num_cols = int(input())

for curr_row in range(1, num_rows + 1):
    curr_col_let = 'A'
    for i in range(1, num_cols + 1):
        print (f'{curr_row}{curr_col_let}', end=' ')
        curr_col_let = chr(ord(curr_col_let) + 1)
    print()