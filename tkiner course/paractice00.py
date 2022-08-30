from sqlite3 import ProgrammingError


# firts Programmig --------------


# dic1={"Mutable":"it is changeable",
# "Imutable":"it is not changeable",
# "Time":"It is very precies",
# "User":"Use your product"}
# for i in dic1:
#  n=input("Enter Here = \n")
#  print(dic1[n])



# secon program \\\\\\\--------------------

# print("Whta do you want to do \n")
# print(" * for mutipication , + for add , - for minus , / for devide , ")
# n=(input("Chose Your sign = \n"))
# x= int( input("Typr your first number \n"))
# y=int( input("Typr your first number \n"))



# if n=="*" :
#     if x==45 and y==3:
#      print("555")
#     else :
#         print(x*y)

# elif n=="+":
#     if x==56 and y==9:
#      print("77")
#     else:
#       print(x+y)
# elif n=="-":
#     print(x-y)    
# elif n=="/":
#     print(x/y)
# else:
#     print("chose again")    


# third program \\\\\\\\\\\\\\\------------------

# n=18
# chance=9
# i=0
# while i< chance:
#     guess=int(input("Guess your number"))

#     if guess<18:
#         print(f"you guess Short number and you have {chance-i} left")
        
#     elif guess>18:
#         print(f"you guess large number and you have {chance-i} left")

#     elif guess==18:
#         print(f"you guess right in {i} chances ")
#         quit()
        
#     else:
#         print("invalid syntaxx try again")   
         
#     i+=1
    
      


# this is fourth project \\\\\\\\\\--------------    



num1=int(input("TYpe your number"))
boll=int(input("1 for true or 0 for false"))
for i in range(num1+1):
    if boll==1:
       
        print("*"*i)
        
    elif boll==0:
        b=num1-i
        print("*"*b)

           