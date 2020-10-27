test_data = list(map(str, range(1, 10, 2)))
print(test_data)

with open("input.txt", "w") as f:
    f.write("\n".join(test_data))

with open("C:/Users/vanis/Downloads/dataset_24465_4 (2).txt", "r") as input_file, \
        open("output.txt", "w") as output_file:
    data = input_file.read().split("\n")
    data.reverse()
    output_file.write("\n".join(data))

with open("output.txt", "r") as f:
    output_data = f.read().split('\n')
test_data.reverse()
print(output_data == test_data)