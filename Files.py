my_file = open(r"C:\Test\routers.txt", "r")
my_file.read()
my_file.seek(0)
my_file.read(5)
my_file.seek(0)
my_file.readline()
my_file.seek(0)
my_file.readlines()
my_file.seek(0)

for line in my_file.readlines():
    if line.startswith("A"):
        print(line.strip())
