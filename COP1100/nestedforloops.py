num_rows = int(input())
num_cols = int(input())

for curr_row in range(num_rows):
    for curr_col_let in range(num_cols):
        print (f'{curr_row}{curr_col_let}', end=' ')
        curr_col_let = chr(ord(curr_col_let) + 1)
    print()