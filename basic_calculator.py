# define the func add, sub, mul, div
# print option to user 
# ask the value
# call the func
# while loop to continue or exit program

def add(a,b):
    answer = a+b
    print(answer)
    print(str(a)+"+"+ str(b)+"="+str(answer)+ "\n")
    # return answer

# print(add(3,2))


def sub(a,b):
    answer = a-b
    print(answer)
    print(str(a)+"-"+ str(b)+"=" +str(answer)+ "\n")
    # return answer

def mul(a,b):
    answer = a*b
    print(answer)
    print(str(a)+"*"+ str(b)+"="+str(answer)+ "\n")
    # return answer

def div(a,b):
    answer = a/b
    print(answer)
    print(str(a)+"/"+ str(b)+"="+str(answer)+ "\n")
    # return answer

while True:
    print("A.addiition")
    print("B.subtraction")
    print("C.multiplication")
    print("D.division")
    print("E.exit")

    choice = input("input your choice:")

    if choice == "A" or choice == "a":
        print("addition")
        a= int(input("input first number:"))
        b= int(input("input seconde number:"))
        add(a,b)
    elif choice == "B" or choice == "b":
        print("subtraction")
        a= int(input("input first number:"))
        b= int(input("input seconde number:"))
        sub(a,b)

    elif choice == "C" or choice == "c":
        print("multiplication")
        a= int(input("input first number:"))
        b= int(input("input seconde number:"))
        mul(a,b)
    elif choice == "D" or choice == "d":
        print("division")
        a= int(input("input first number:"))
        b= int(input("input seconde number:"))
        div(a,b)


    elif choice == "E"  or choice == "e":
        print("exit")
        quit()




