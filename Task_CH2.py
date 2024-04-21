'''
This is the solve for taks_1 in cahpter 2
'''
# Answer the quistion P1
Name = "Ayman"
Age = '19'
Country = 'Egypt'
print('Name:',Name)
print('Age:',Age)
print('Country:',Country)
'''
Output For part:1:
Name: Ayman
Age: 19
Country: Egypt
'''
#by two ways
Concatenate_var = 'Hello, My Name Is ' + Name + ' And Iam ' + Age + ' Years old and I Live in ' + Country + '.'
print(Concatenate_var)
print(f"Hello, My Name Is {Name} And Iam {Age} Years old and I Live in {Country}.")
# Output : Hello, My Name Is Ayman And Iam 19 Years old and I Live in Egypt.

print(type(Name))
print(type(Age))
print(type(Country))
'''
Output:
<class 'str'>
<class 'str'>
<class 'str'>
'''
#-----------------------------------------------------------------------------------------------------------

#Answer the quistion p2
Name = "Ayman"
Age = '19'
Country = 'Egypt'
print("\"Hello '" + Name + "', How You Doing \\ \"\"\" Your Age Is \"" + Age + "\" + And Your Country Is: " + Country)
# output: "Hello 'Ayman', How You Doing \ """ Your Age Is "19" + And Your Country Is: Egypt
print("\"Hello '" + Name + "', How You Doing \\ \n\"\"\" Your Age Is \"" + Age + "\" + \nAnd Your Country Is: " + Country)
'''
output:
"Hello 'Ayman', How You Doing \
""" Your Age Is "19" +
And Your Country Is: Egypt
'''
name = "Elzero"
Second_letter = name[1]
Third_letter = name[2]
Last_letter = name[-1]

print(f"Second Letter Is \"{Second_letter}\"")
print(f"Third Letter Is \"{Third_letter}\"")
print(f"Last Letter Is \"{Last_letter}\"")
'''
Output:
Second Letter Is "l"
Third Letter Is "z"
Last Letter Is "o"
'''
part1 = name[1:4]
part2 = name[0:2] + name[3]
part3 = name[2] + name[3] + name[0]
print(f"\"{part1}\"")
print(f"\"{part2}\"")
print(f"\"{part3}\"")
'''
output:
"lze"
"Ele"
"zeE"
'''
name1 = "#@#@Elzero#@#@"
withoutChar = name.strip("#@")  #usnig .strip to remove # and @ 
print(withoutChar)
#output: Elzero

num1 = "5"
num2 = "22"
num3 = "456"
num4 = "1908"
print(num1.zfill(4)) # using .zfill method to fill the left of the number with zeros
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4)) 
'''
output:
0005
0022
0456
1908
'''
name_one = "Osama"
name_two = "Osama_Elzero"
name_oneAfter = "@" * (20 - len(name_one)) + name_one
name_twoAfter = "@" * (20 - len(name_two)) + name_two
print(name_oneAfter)
print(name_twoAfter)
#output:@@@@@@@@@@@@@@@Osama 
#output:@@@@@@@@Osama_Elzero

name3 = "OSamA"
name4 = "osaMA"
print(name3.swapcase())
print(name4.swapcase())
'''
output:
osAMa
OSAma
'''
msg = "I Love Python And Although Love Elzero Web School And Love Momen Walied (^_^)"
print(msg.count("Love"))
#output: 3

name5 = "Elzero"
print(name5.index("z"))
#output : 2

msg2 = "I <3 Python And Although <3 Elzero Web School And <3 Momen Walied (^_^)"
print(msg2.replace("<3","Love",1))
#output: I Love Python And Although <3 Elzero Web School And <3 Momen Walied (^_^)
print(msg2.replace("<3","Love"))
#output:I Love Python And Although Love Elzero Web School And Love Momen Walied (^_^)

Name1 = "Ayman"
Age1 = 19
Country1 = 'Egypt'

print(f"My Name Is {Name1}, And My Age Is {Age}, And My Country Is {Country1}")
#output: My Name Is Ayman, And My Age Is 19, And My Country Is Egypt

#--------------------------------------------------------------------------------------------
#Answering quistion P3

print("Integer numbers:")
print(222)

print("Floating-point numbers:")
print(11.2)

print("Complex numbers:")
print(5 - 3j)
'''
output:
Integer numbers:
222
Floating-point numbers:
11.2
Complex numbers:
(5-3j)
'''
number = 1+2j
print("Imaginary Part: ",number.imag)
print("Real Part: ",number.real)
'''
output:
Imaginary Part:  2.0
Real Part:  1.0
'''
number2 = 10
print( f"{number2:.10f}") #output: 10.0000000000

number3 = 159.650
number3 = int(number3)
print(number3) #output:159
print(type(number3)) #output:<class 'int'>
'''
100 - 115 = -15
50 * 30 = 1500
21 % 4 = 1
int(110 / 11) = 10
97 // 20 = 4
'''
#Check the output
print(100 - 115)
print(50 * 30)
print(21 % 4)
print(int(110 / 11))
print(97 // 20)
