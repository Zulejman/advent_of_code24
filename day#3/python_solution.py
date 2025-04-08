import re

uncorr_line = []
total_value = 0

#part 1
with open("input.txt", "r") as file_data:
    for line in file_data:
        uncorr_line = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
        for data_entry in uncorr_line:
            multy = int(data_entry[0]) * int(data_entry[1])
            total_value += multy


file_data.close()
print(total_value)

