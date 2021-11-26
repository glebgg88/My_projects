from platform import python_version,processor,architecture 
FILE_NAME = "Your system info.txt"

def python_v():
    return "Your python version: {}".format(python_version())

def proc():
    return "Your processor: {}".format(processor())

def os():
    bits = architecture()
    return bits

while True:
    print("Select operation: python version,os,processor,exit")
    choice = input()

    if choice == "exit":
        print("I hope you liked it")
        break
    elif choice == "python version":
        print(python_v())
    elif choice == "os":
        print(os())
    elif choice == "processor":
        print(proc())
    else:
        print("Incorrect data specified")