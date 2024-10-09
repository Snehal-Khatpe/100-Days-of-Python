# Create a calculator capable of performing addition, subtraction,
# multiplication and division operations on two numbers.
# Your program should format the output in a readable manner!


value1 = float(input("Enter value1: "))
value2 = float(input("Enter value2: "))

Select_operator = input("Select any operator from  +, _, *, /:  ")


if Select_operator == '+':
    result = value1 + value2
elif Select_operator == '-':
    result = value1 - value2
elif Select_operator == '*':
    result = value1 * value2
else:
    result = 'Invalid Operator'


print(result)
