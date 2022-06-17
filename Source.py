
def getdate():
    import datetime
    return datetime.datetime.now()

def DietFile(choice):
    if choice == 1:
        f = open("SubhanDiet.txt", "a")
        print("Enter the diet you want to enter in the file.")
        diet = input()
        str2 = "[" + str(str(getdate())) + "]" + diet
        f.write(str2)
        f.close()
    if choice == 2:
        f = open("HassaanDiet.txt", "a")
        print("Enter the diet you want to enter in the file.")
        diet = input()
        str2 = "[" + str(str(getdate())) + "]" + diet
        f.write(str2)
        f.close()
    if choice == 3:
        f = open("AhmadDiet.txt", "a")
        print("Enter the diet you want to enter in the file.")
        diet = input()
        str2 = "[" + str(str(getdate())) + "]" + diet
        f.write(str2)
        f.close()

def ExcerciseFile(choice):
    if choice == 1:
        f = open("SubhanExcercise.txt", "a")
        print("Enter Excercise you want to enter : ")
        excercise = input()
        dateandTime = str(str(getdate()))
        str1 = "[" + dateandTime + "]" + excercise
        f.write(str1)
        f.close()
    if choice == 2:
            f = open("HassaanExcercise.txt", "a")
            print("Enter Excercise you want to enter : ")
            excercise = input()
            dateandTime = str(str(getdate()))
            str1 = "[" + dateandTime + "]" + excercise
            f.write(str1)
            f.close()
    if choice == 3:
            f = open("AhmadExcercise.txt", "a")
            print("Enter Excercise you want to enter : ")
            excercise = input()
            dateandTime = str(str(getdate()))
            str1 = "[" + dateandTime + "]" + excercise
            f.write(str1)
            f.close()


def fileWrite(choice):
        print("Enter 1 for write in excercise file and 2 for write in diet file.")
        fileChoice = int(input())
        if fileChoice == 1:
            ExcerciseFile(choice)
        elif fileChoice == 2:
            DietFile(choice)


def readExcerciseFile(choice):
    if choice == 1:
        from os.path import exists
        file_exists = exists("SubhanExcercise.txt")
        if file_exists == True:
            with open("SubhanExcercise.txt") as SubhanExcercise:
                fileRead = SubhanExcercise.read()
                print(fileRead)
        else:
            print("\"Subhan Excercise\" does not exist.")
    elif choice == 2:
        from os.path import exists
        file_exists = exists("HassaanExcercise.txt")
        if file_exists == True:
            with open("HassaanExcercise.txt") as HassaanExcercise:
                print(HassaanExcercise.read())
        else:
            print("\"Hassaan Excercise\" does not exist.")
    elif choice == 3:
        from os.path import exists
        file_exists = exists("AhmadExcercise.txt")
        if file_exists == True:
            with open("AhmadExcercise.txt") as AhmadExcercise:
                print(AhmadExcercise.read())
        else:
            print("\"Ahmad Excercise\" does not exist.")

def readDietFile(choice):
    if choice == 1:
        from os.path import exists
        file_exists = exists("SubhanDiet.txt")
        if file_exists == True:
            with open("SubhanDiet.txt") as SubhanDeit:
                print(SubhanDeit.read())
        else:
            print("\"Subhan Diet\" does not exist.")
    elif choice == 2:
        from os.path import exists
        file_exists = exists("HassaanDiet.txt")
        if file_exists == True:
            with open("HassaanDiet.txt") as HassaanDeit:
                print(HassaanDeit.read())
        else:
            print("\"Hassaan Diet\" does not exist.")
    elif choice == 3:
        from os.path import exists
        file_exists = exists("AhmadDiet.txt")
        if file_exists == True:
            with open("AhmadDiet.txt") as AhmadDeit:
                print(AhmadDeit.read())
        else:
            print("\"Ahmad Diet\" does not exist.")

def fileRead(choice):
    print("Enter 1 for read from Excercise file and 2 for read from diet file.")
    fileChoice = int(input())
    if fileChoice == 1:
        readExcerciseFile(choice)
    elif fileChoice == 2:
        readDietFile(choice)

print("Enter 0 If you want to read data from files and 1 if you want to write data to files.")
read_Or_Write = int(input())
if read_Or_Write == 0:
    print("Enter 1 for Subhan\nEnter 2 for Hassaan\nEnter 3 for Ahmad")
    person_Choice = int(input())
    fileRead(person_Choice)

elif read_Or_Write == 1:
    print("Enter 1 for Subhan\nEnter 2 for Hassaan\nEnter 3 for Ahmad")
    person_Choice = int(input())
    fileWrite(person_Choice)



