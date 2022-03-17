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

new_file = open(r"C:\CoreQA\newfile.txt", "w")
new_file.write("I like Python!\nDo you?")
new_file.close()

with open(r"C:\CoreQA\newfile.txt", "w") as f:
    f.write('Hello, Python!')

with open(r"C:\CoreQA\newfile.txt", "a") as f:
    f.write("\nWelcome")

with open(r"C:\CoreQA\newfile.txt", "r+") as f:
    f.truncate(10)