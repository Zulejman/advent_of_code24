

with open("input.txt", "r") as data_file:
    lines_array = []
    line_len = 0
    rows_number = 0

    for line in data_file:
        rows_number += 1
        lines_array.append(line[:-2])

    line_len = len(line)


    padding = "P" * (line_len - 2)
    lines_array.insert(0, padding)
    lines_array.append(padding)

    padded_array = []

    for line in lines_array:
        padded_array.append("P" + line + "P")

    for line in padded_array:
        print(line)

    word = "XMAS"

    for xmask in range(1, len(padded_array[0]) - 1):
        for ymask in range(1, rows_number - 1):
            if padded_array[xmask][ymask] == "X":


#Probaj sa generiranjem teksta u svim smjerovima
