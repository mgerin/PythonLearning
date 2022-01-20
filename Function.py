# Functions
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old")


say_hi("Marin", 32)
say_hi("Lyubo", 30)


def cube(num):
    return num*num*num


result = cube(5)
print(result)


def my_first_function(x, y, z):
    sum_xyz = (x + y) * z
    return sum_xyz


my_first_function(1, 2, 3)
my_first_function(x = 1, z = 3, y = 2)


def my_second_function(x, y, z = 3):
    sum_xyz = (x + y) * z
    return sum_xyz


my_second_function(1, 2)


def args_function(x, *args):
    print(x)
    for argument in args:
        print(argument)


args_function("hello")
args_function("hello", 100, 200)


def my_var_func():
    my_var = 10
    print(my_var)


my_var_func()
my_var = 20
print(my_var * 10)


my_var1 = 5


def my_new_var_func():
    global my_var1
    print(my_var1)
    my_var1 = 10


my_new_var_func()


def my_third_func():
    my_new_var = 10
    print(my_new_var)
    return my_new_var


result = my_third_func()

print(result * 10)


# Coding Exercise 33
def my_print_func():
    print("I am becoming a Python developer!")


my_print_func()


# Coding Exercise 34
def myfunc(x, y):
    result = (x ** y) + 500
    return result


print(myfunc(10, 3))


# Coding Exercise 35
var1 = 100


def var1_func():
    global var1
    print(var1 * 10)
    var1 = 200


var1_func()

# If statements
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