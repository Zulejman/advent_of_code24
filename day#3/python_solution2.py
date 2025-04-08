import re

uncorr_line = []
uncorr_copy = []
total_value = 0

with open("input.txt", "r") as file_data:

        mul_enabled = True

        for line in file_data:
            instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line)

            for instr in instructions:
                if instr == "do()":
                    mul_enabled = True  
                elif instr == "don't()":
                    mul_enabled = False  
                elif instr.startswith("mul(") and mul_enabled:
                    values = re.search(r"mul\((\d+),(\d+)\)", instr)
                    if values:
                        val1, val2 = int(values.group(1)), int(values.group(2))
                        total_value += val1 * val2

           
    


file_data.close()

print(total_value)
