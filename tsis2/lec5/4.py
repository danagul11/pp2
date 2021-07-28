a_file = open("example.txt", "r")
lines = a_file. readlines()
last_lines = lines[-5:]
print(last_lines)