n_rows = int(input())
nri = n_rows 
while nri > 0:
    row_lenght = int(input())
    row_data = input()
    i = 0
    forbid_n = []
    for l in row_data:
        if not (row_lenght - 1) == i:
            if str(row_data[i]) + str(row_data[i + 1]) == "()" and not i in forbid_n:
                forbid_n.extend([i, i + 1])
        i += 1
    for l in row_data:
        if
    print(forbid_n)
    nri -= 1
    print("row number " + str(nri))