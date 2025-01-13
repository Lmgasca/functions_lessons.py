
# functions are ways to wrap your codes 
# into reuseable units

# how you define a function
# I only define the function ONCE.
# whatever I pass inside the parantheses
# is called a parameter
#a parameter is a placeholder for future information

# def sayHello(name, age, address):
#     print(f"say hello {name}")
#     print(f"Hello Governor, your address is {address}")
#     print(f"welcome back {name}")
#     print(f"your age is {age}") 

# # once you define a function 
# # you must call or invoke the function
# # when I pass in information into the 
# # the called function, its called an argument
# sayHello("evins", 34,"345 north lawndale" )
# sayHello("Devin", 25, "345 south lawndale")
# sayHello("Lara", 45, "345 west lawndale")

# def determinEligibility(age)
#     # if your age is over 18, you can vote,
#     # otherwise you cant
#     if age >= 18:
#         print("ypu can vote")
#     else:
#         print("you have to wait")

# determinEligibility(12)
# determinEligibility(15)
# determinEligibility(19)

# def willYouGraduate(gpa, credits, SAT):
#     #gpa: number variable
#     #credits: number variable
#     #passed SAT: BOOLEAN
#     if (gpa >= 3.0) and (credits >= 28) and (SAT == True):
#         print("you passed. Good luck in college")
#     elif (gpa < 3.0) or (credits < 28) or (SAT != True):
#         print("talk to your counselor")

# willYouGraduate(2.8, 15, True)
# willYouGraduate(3.6, 30, False)
# willYouGraduate(4.3, 32, True)



# # return = statement used to end a function
# #          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z
 
# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))



def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("spongebob", "squarepants")
print(full_name)