print("hello world") 
y={"name":"paul"}
print(type(y))
x={"name":"benyi"}
print(type(x))
name="gracious"
age=18
city="bamenda"
hobby= "dancing"
print(f"my name is {name} i am {age} years old \n  i live in {city}i love {hobby}")
#exercise 2 
length=10
width=5
area= length * width 
perimeter = (length + width)*2
print(f"the area and perimeter of the rectangle:{length} and {width} is area and perimeter respectively")
#exercise 3 
celsius = 25 
fahrenheit=(celsius*9/5) + 32
print(f"the temperature in celsius {celsius} and temperature in fahrenheit {fahrenheit}")
name= """benyi loves eating
she loves eating they lov eating we lobve eating he or she"""
print ("hello\n"*12 ,end="")
city="bamenda"
print(f"number of letters is = {len(city)}") 
print(city[-1])
print(city[0:3])
print(city[-1:-5:-1])
print(city[0:])
name="saturday"
new_name= name.upper()
print(f"old:{name}\nnew:{new_name}")
f_name = "JOHN doe"
print("".join(f_name.title().split()))
age = 56
if age >=50:
    print("you are a youth")
    password = "secre123"
    user_input = "secre123"
    if password == user_input:
            print("acess granted!")
            print("welcome to the system!")
    else:
            print("acess denied!")
            print("incorrect password!")
            
