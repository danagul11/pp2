def txt_read(file_name):
    txt = open(file_name)
    print(txt.read())

txt_read('test.txt')