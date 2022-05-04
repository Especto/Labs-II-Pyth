from functions import *

def main():
    inFile = input("Enter file 1 path: ")
    outFile = input("Enter file 2 path: ")
    create_file(inFile)
    enter_file(inFile)
    listT = read_file(inFile)
    print("\nList of Techniques: \n")
    print_list(listT)
    expired(listT, outFile)
    listExp = read_file(outFile)
    print("\nList of expired Techniques: \n")
    print_list(listExp)

main()
