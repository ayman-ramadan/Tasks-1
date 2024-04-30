#P1_Q1
#True prints
print(bool("Osama"))
print(bool(100>50))
print(bool([1, 2, 3]))
print(bool(100))
#False prints
print(bool(0))
print(bool(100<50))
print(bool([]))
print(bool())
'''
True
True
True
True
False
False
False
False
'''
#P1_Q2
html = 90
css = 70
javascript = 60
print(html > 50 and css > 50 and javascript > 50) #True

#P1_Q3
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two) #True
print(num > num_one and num > num_two) #False

#P1_Q4
num_one = 10
num_two = 20

result = num_one + num_two
print(result)

exponent = result ** 3
print(exponent)

remainder = exponent % 26000
print(remainder)

divisionResult = remainder / 5
print(divisionResult)

print(type(str(divisionResult)))
'''
30
27000
1000
200.0
<class 'str'>
'''
#-----------------------------------------------------------------------------------------------------------------------------
#P2_Q1
name =input("Enter Your Name: ") #Enter Your Name:      ayMan 
name = name.strip().capitalize()
print(f"Hello {name}, Happy To See You Here.") #Hello Ayman, Happy To See You Here.

#P2_Q2
age = int(input("Enter Your Age : "))
# Check if the input age is less than 16
if age < 16:
    print("Hello, your age is under 16. Some articles are not suitable for you.")# Hello, your age is under 16. Some articles are not suitable for you.
else:
    print(f"Hello, your age is {age}. All articles are suitable for you.") #Hello, your age is 20. All articles are suitable for you.
    
#P2_Q3
first_name = input("Enter your first name: ").strip().capitalize()
second_name = input("Enter your second name: ").strip().capitalize()
first_letter_second_name = second_name[0]
print(f"Hello {first_name} {first_letter_second_name}.")
'''
Enter your first name: aaa
Enter your second name: weq
Hello Aaa W.
'''

#P2_Q3
email = input("Enter your email: ").strip().lower()
name = email.split('@')[0].capitalize()
provider = email.split('@')[1].split('.')[0]
top_domain = email.split('.')[-1]

# Print the formatted messages
print(f"Your name is {name}")
print(f"Email service provider is {provider}")
print(f"Top level domain is {top_domain}")
'''
Enter your email: qrrqw@qwe
Your name is Qrrqw
Email service provider is qwe
Top level domain is qrrqw@qwe
'''
#-------------------------------------------------------------------------------------------------------------------------------------------

#P3_Q1
# Store the input numbers and operation
num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())
operation = input("Enter the operation (+, -, *, /, %): ").strip()
#choose what is the operator should use
if operation == "+":
    result = num1 + num2
    operator = "+"
elif operation == "-":
    result = num1 - num2
    operator = "-"
elif operation == "*":
    result = num1 * num2
    operator = "*"
elif operation == "/":
    result = num1 / num2
    operator = "/"
elif operation == "%":
    result = num1 % num2
    operator = "%"
else:
    print("Invalid operation")
    exit()

# Print the formatted result
print(f"{num1} {operator} {num2} = {result}")
'''
Enter the first number: 5
Enter the second number: 6
Enter the operation (+, -, *, /, %): +
5 + 6 = 11
'''
#P3_Q2
age = 17
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You") #App Is Suitable For You

#P3_Q3
age2 = int(input("Enter your age: "))
if 10 < age2 < 100:
    months = age2 * 12
    weeks = age2 * 52
    days = age2 * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    # Print age in different units
    print(f"Your age in months is {months} months")
    print(f"Your age in weeks is {weeks} weeks")
    print(f"Your age in days is {days} days")
    print(f"Your age in hours is {hours} hours")
    print(f"Your age in minutes is {minutes} minutes")
    print(f"Your age in seconds is {seconds} seconds")
else:
    print("Your age is out of range (10-100 years).")
    
'''
Enter your age: 50
Your age in months is 600 months
Your age in weeks is 2600 weeks
Your age in days is 18250 days
Your age in hours is 438000 hours
Your age in minutes is 26280000 minutes
Your age in seconds is 1576800000 seconds
'''

#P3_Q4
country = input("Enter your country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "Ksa", "Bahrain"]
price = 100
discount = 30
#check if it have discount or not
if country in countries:
    # Calculate discount
    discountPrice = price - discount
    print(f"Your country is eligible for a discount and the price after discount is ${discountPrice}")
else:
    print(f"Your country is not eligible for a discount and the price is ${price}")
    
'''
Enter your country: Egypt
Your country is eligible for a discount and the price after discount is $70
'''