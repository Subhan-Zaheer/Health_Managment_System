
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
    if choice == 1:
        print("Enter 1 for write in excercise file and 2 for write in diet file.")
        fileChoice = int(input())
        if fileChoice == 1:
            ExcerciseFile(choice)
        elif fileChoice == 2:
            DietFile(choice)


print("Enter 0 If you want to read data from files and 1 if you want to write data to files.")
read_Or_Write = int(input())
if read_Or_Write == 0:
    print("Enter 1 for Subhan\nEnter 2 for Hassaan\nEnter 3 for Ahmad")
    person_Choice = int(input())
    if person_Choice == 1:
        print("Enter 0 if you want to read diet of Subhan and 1 if you want to read excercise of Subhan.")
        fileChoice = int(input())
        if fileChoice == 0:
            from os.path import exists
            file_exists = exists("SubhanDiet.txt")
            if file_exists == True:
                with open("SubhanDiet.txt") as SubhanDeit:
                    SubhanDeit.read()
            else:
                print("\"Subhan.txt\" does not exist.")

        elif fileChoice == 1:
            from os.path import exists
            file_exists = exists("SubhanExcercise.txt")
            if file_exists == True:
              with open("SubhanExcercise.txt") as SubhanExcercise:
                  fileRead = SubhanExcercise.read()
                  print(fileRead)
            else:
                print("\"Subhan Excercise\" does not exist.")
    if person_Choice == 2:
        print("Enter 0 if you want to read diet of Hassaan and 1 if you want to read excercise of Hassaan.")
        fileChoice = int(input())
        if fileChoice == 0:
            from os.path import exists
            file_exists = exists("HassaanDiet.txt")
            if file_exists == True:
                 with open("HassaanDiet.txt") as HassaanDeit:
                    HassaanDeit.read()
            else:
                print("\"Hassaan Diet\" does not exist.")
        elif fileChoice == 1:
            from os.path import exists
            file_exists = exists("HassaanExcercise.txt")
            if file_exists == True:
                with open("HassaanExcercise.txt") as HassaanExcercise:
                    HassaanExcercise.read()
            else:
                print("\"Hassaan Excercise\" does not exist.")
    if person_Choice == 3:
        print("Enter 0 if you want to read diet of Ahmad and 1 if you want to read excercise of Ahmad.")
        fileChoice = int(input())
        if fileChoice == 0:
            from os.path import exists
            file_exists = exists("AhmadDiet.txt")
            if file_exists == True:
                with open("AhmadDiet.txt") as AhmadDeit:
                    AhmadDeit.read()
            else:
                print("\"Ahmad Diet\" does not exist.")
        elif fileChoice == 1:
            from os.path import exists
            file_exists = exists("AhmadExcercise.txt")
            if file_exists == True:
                with open("AhmadDiet.txt") as AhmadExcercise:
                    AhmadExcercise.read()
            else:
                print("\"Ahmad Excercise\" does not exist.")

elif read_Or_Write == 1:
    print("Enter 1 for Subhan\nEnter 2 for Hassaan\nEnter 3 for Ahmad")
    person_Choice = int(input())
    fileWrite(person_Choice)



