with open("new_file", "w+") as f:
    write_data = "Hello world!"
    f.write(write_data)

with open("new_file" , "r") as f:
    read_data = f.read()

print(read_data)