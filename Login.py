from pathlib import Path
from TestText import *


print('Welcome to my super secret password holder')
User = input('First, my program has to make sure its me: ' )
filepath = "C:\\Users\\dylan\\Python\\Login system\\"
PassWD = input('Next, the password of course, this is the password to end all passwords: ')
Password = input('Reenter password: ') 
filename =  User + '.txt' 
filenameText =  User +'1.txt'
filenamePath = filepath+filename
fileTextPath = filepath+filenameText

def Login():
    txt = Path(filenamePath).read_text()
    #Password Checker for passwords that are too short
    if Password != txt:
     print('Wrong password there buddy')
     return 0
    if PassWD == Password:
        #Defines full text
        print('Getting variable...\n\n\n')
        myfile = open(filenamePath, 'r')
        for line in myfile:
         #If the password (PassWD) matches the line in myFile, then activate the text file holding the passwords
         if (PassWD) in line:
            myfile.close
            print('Activating password file...\n\n\n')    
            textFile = open(fileTextPath, 'r') 
            print(textFile.read())
            textFile.close
            return 0
            
         else:
          print('failure')
          myfile.close
          return 0


def reg():
  choice = input("Do you really want to create a new file[y/n]: ")
  if choice == 'y':
    newFile = open(filenameText, 'w+')
    passwordFile = open(filename, 'w+')
    passwordFile.write(Password)
    passwordFile.close
    newFile.close
  elif choice == 'n':
    return 0

def add():
  #Lets you look at the file content
  appendFile = open(fileTextPath, 'r')
  print(appendFile.read())
  appendFile.close
  #Then lets you append whatever you want to it
  appendFile = open(fileTextPath, 'a')
  add = input("Add whatever you want to the file: ")
  #Final check if you messed up 
  choice = input("Are you sure you want to add this[y/n]: ")
  if choice == "y":
    appendFile.append(add)
    appendFile.close
  elif choice == "n":
    appendFile.close
    return 0

#Choice at start of program
loginish = input('Are you logging in[a], registering?[b], or adding to a file[c]?: ')
if loginish == "a":
 Login()
elif loginish == "b":
 reg()
elif loginish == "c":
 add()



    

