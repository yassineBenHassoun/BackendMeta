# Using explicit type conversion, change the following 
# inputs so the types match with the following below
#  
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

# Modify the line below
getName = input('What is your name? ')

name = str(getName)

print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# Modify the line below
getAge = input('What is your age? ')

age = int(getAge)
print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# Modify the line below
getHeight = input('What is your height in meters? ')
height = float(getHeight)

print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# Modify the line below
l = input('Are you part of our loyalty program? ')
loyalty = bool(l)

print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")

