

def dataPrepare(file_name):

    level_arrays = []

    with open(file_name, "r+") as data_file:
        for line in data_file:
            letter_values = list(map(int, line.split()))
            level_arrays.append(letter_values)

    data_file.close()
    return level_arrays

def is_safe(report):
    increasing = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if not (1 <= abs(diff) <= 3):
            return False

        if diff > 0:  
            if increasing is False:  
                return False
            increasing = True
        elif diff < 0:  
            if increasing is True: 
                return False
            increasing = False
        else:  
            return False

    return True

def main():
    reports = dataPrepare("input.txt")
    total_safe = 0

    for report in reports:
        if is_safe(report):
            total_safe += 1

    print(total_safe)

if __name__ == "__main__":
    main()
