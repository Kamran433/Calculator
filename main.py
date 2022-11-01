
# from replit import clear
# import cal_logo
# def div(a,b):
#   c=a/b
#   print(f"{a}/{b}={c}")
#   print(f"The result is : {c}")
#   return c
# def mult(a,b):
#   c=a*b
#   print(f"{a}*{b}={c}")
#   print(f"The result is : {c}")
#   return c
# def sub(a,b):
#   c=a-b
#   print(f"{a}-{b}={c}")
#   print(f"The result is : {c}")
#   return c
# def add(a,b):
#   c=a+b
#   print(f"{a}+{b}={c}")
#   print(f"The result is : {c}")
#   return c
# print(cal_logo.logo)
# exp1=float(input("enter first number :"))
# opr=input("enter any one operation:\n1. +\n2. -\n3. *\n4. /\nEnter any option?\n")
# exp2=float(input("enter second number :"))
# c=""
# if opr=="+":
#   c=add(exp1,exp2)
# elif opr=="-":
#   c=sub(exp1,exp2)
# elif opr=="*":
#   c=mult(exp1,exp2)
# elif opr=="/":
#   c=div(exp1,exp2)
# cont=True

# while cont==True:
#   st=input(f"Type 'y' to continue calculating with {c}, or type 'n' to start a new calculation: ")
#   if st=="y":
#    opr=input("enter any one operation:\n1. +\n2. -\n3. *\n4. /\nEnter any option?\n")
#    exp2=float(input("enter second number :"))
#    if opr=="+":
#     add(c,exp2)
#    elif opr=="-":
#     sub(c,exp2)
#    elif opr=="*":
#     mult(c,exp2)
#    elif opr=="/":
#     div(c,exp2)
#   elif st=="n":
#    clear()
#    print(cal_logo.logo)
#    exp1=float(input("enter first number :"))
#    opr=input("enter any one operation:\n1. +\n2. -\n3. *\n4. /\nEnter any option?\n")
#    exp2=float(input("enter second number :"))
#    if opr=="+":
#      add(exp1,exp2)
#    elif opr=="-":
#      sub(exp1,exp2)
#    elif opr=="*":
#      mult(exp1,exp2)
#    elif opr=="/":
#      div(exp1,exp2)
