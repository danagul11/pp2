  
def file_read(file_name):
    with open(file_name) as f:
        output_list = f.readlines()
        print(output_list)

file_read('test.txt')