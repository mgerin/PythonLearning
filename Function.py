#Functions
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old")

say_hi("Marin", 32)
say_hi("Lyubo", 30)

def cube(num):
    return num*num*num

result = cube(5)
print(result)

#If statements
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male or tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("You are not male but are tall")
else:
    print("You are not male and not tall")