def file_writer(file_name):
    from itertools import islice
    with open(file_name, 'w') as file:
        file.write("Erkin S. Baizhanov\n")
        file.write("Student of KBTU:)")
    txt = open(file_name)
    print(txt.read())

file_writer('abc.txt')