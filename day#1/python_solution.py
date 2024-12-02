left_list = []
right_list = []
id_distances = []

with open("input.txt", "r+") as data_file:

    for line in data_file:
        left_id = line[:5]
        right_id = line[5:].strip()
        left_list.append(int(left_id))
        right_list.append(int(right_id))

data_file.close()

left_list.sort()
right_list.sort()

for i in range(0, len(left_list)):
    iter_distance = abs(left_list[i] - right_list[i])
    id_distances.append(iter_distance)

print(sum(id_distances))
