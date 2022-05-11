# Calculator Made By Anoop Singh Nagi

print("""ASN Calculator

It can be add, subtract, multiply and divide two numbers...

""")

# Variables
first_num = int(input("Enter First Number: "))
opt_sign = input("Enter Operation Sign: ")
sec_num = int(input("Enter Second Number: "))
print("")

"""
If Else Conditions For:

1. Addition
2. Subtraction
3. Multiplication
4. Divison
"""

# For Addition
if opt_sign == "+":
    print("Your Answer is",first_num + sec_num)

elif opt_sign == "Add":
    print("Your Answer is",first_num + sec_num)

elif opt_sign == "add":
    print("Your Answer is",first_num + sec_num)


# For Subtraction
elif opt_sign == "-":
    print("Your Answer is",first_num - sec_num)

elif opt_sign == "Minus":
    print("Your Answer is",first_num - sec_num)

elif opt_sign == "minus":
    print("Your Answer is",first_num - sec_num)


# For Multiplication
elif opt_sign == "*":
    print("Your Answer is",first_num * sec_num)

elif opt_sign == "Multiply":
    print("Your Answer is",first_num * sec_num)

elif opt_sign == "multiply":
    print("Your Answer is",first_num * sec_num)


# For Division
elif opt_sign == "/":
    print("Your Answer is",first_num / sec_num)

elif opt_sign == "Divide":
    print("Your Answer is",first_num / sec_num)

elif opt_sign == "divide":
    print("Your Answer is",first_num / sec_num)


# If Operator is not vaild, else condition will be applied
else:
    print("'",opt_sign, "'", "is not a vaild operator...")


"""
Python Calculator Made By Anoop Singh Nagi
Commercial use only, No use for Examination. It will show your dishonesty.

Copyright ASN 2022
"""
