import pickle
from Technic import Technic

def create_file(inFile):
    check = input("Enter 'a' to add information or enter 'n' to create new file: ")
    file = open(inFile, "ab" if check == "a" else 'wb')
    file.close()


def write_to_file(inFile, name, date_buy, guarantee):
    with open(inFile, "ab") as file:
        pickle.dump(name, file)
        pickle.dump(date_buy, file)
        pickle.dump(guarantee, file)


def read_file(file_path):
    list = []
    with open(file_path, "rb") as file:
        while True:
            try:
                name = pickle.load(file)
                date_buy = pickle.load(file)
                guarantee = pickle.load(file)
                tech = Technic(name, date_buy, guarantee)
                list.append(tech)
            except EOFError:
                break
    return list

def enter_file(file_path):
    n = int(input("Input number of techniquec: "))
    print("Enter list of techniques: ")
    for i in range(n):
        name = input("Name of technique: ")
        date_buy = input("Date of buy (dd.mm.yyyy): ")
        guarantee = input("Days Warranty: ")
        write_to_file(file_path, name, date_buy, guarantee)

def print_list(listT):
    for tech in listT:
        print(tech.get_info())


def expired(listT, file_path):
    file = open(file_path, "wb")
    file.close()
    for tech in listT:
        if tech.is_guarantee():
            write_to_file(file_path, tech.name, tech.date_buy, tech.guarantee)
