num1 = 4  ;  num2 = 6  ;  op = "*"
if op=="+": result = num1 + num2
elif op=="-": result= num1 - num2
elif op=="*": result = num1 * num2
elif op=="//": result = num1 // num2
elif op=="%" : result = num1 % num2 
elif op=="**": 
    if num2 != 0: result = num1 / num2
    else:         result = "Error: division by zero"
else: result = "Error: unknown operation"

print(f"{num1} {op} {num2} = {result}")