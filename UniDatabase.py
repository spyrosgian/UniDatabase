# A. Importing "Open" from "Shelve"

from shelve import open

# B. Defining all the functions regarding inputs type that will be used at diffenrent stages of the script

# B. 1. Check if inputs are alphabetic characters

def checkalpha (prompt, message):

    while True:

        data = input (prompt)

        if not data.isalpha():
            print (message)
            continue

        break

    return data

# B. 2. Check if inputs are decimal digits

def checkdecimal (prompt, message1):

    while True:

        data = input (prompt)
        if not data.isdigit():
            print (message1)
            continue
        
        break

    return data

# B. 3. Check if inputs are decimal digits or more than limit

def checkdecimalmark (prompt, message1, message2):

    while True:

        data = input (prompt)
        if not data.isdigit():
            print (message1)
            continue
        if int (data) > 100:
            print (message2)
            continue

        break

    return data

# B. 4. Check if module name is in the right format

def checkmod (prompt, message):

    while True:

        data = input (prompt)

        if len (data) != 6:
            print (message)
            continue

        start2 = data [0:2] # 2 first characters
        end4   = data [2: ]  # 4 last characters

        if not start2.isalpha() or not end4.isdigit():
            print (message)
            continue

        break

    return data

# C. Defining all the functions regarding "Menu" and "Database" that will be used at diffenrent stages of the script

# C. 1. Add record to database function

def addtodb ():

    os.system ('cls')
    
    List1 = [] # Creating and empty list

    key = checkdecimal ('Student Number: ' , 'Decimal digits')
    List1.append (key)

    title = checkalpha ('Student Title: ' , 'Alphabetic characters')
    List1.append (title)

    forename = checkalpha ('Forname: ' , 'Alphabetic characters')
    List1.append (forename)

    surname = checkalpha ('Surname: ' , 'Alphabetic characters')
    List1.append (surname)

    module = checkmod ('Module: ' , 'Module Format: CE1234')
    List1.append (module)

    coursemark = checkdecimalmark ('Coursemark: ' , 'Decimal digits' , 'Mark cannot be bigger than 100')
    List1.append (coursemark)

    exammark = checkdecimalmark ('Exammark: ' , 'Decimal digits', 'Mark cannot be bigger than 100')
    List1.append (exammark)

    data = ' '.join(List1) # Joining all inputs of the list and creating a single input/line

    db = open (module)

    if key in db: # Checking if student already exists in the current database
        print ('')
        print ("Student '%s' already exists in database" % key)
    else:
        db [key] = data
        print ('')
        print ("Student '%s' added to database" % key)

    db.close ()

    print ('')
    key = input ('\n\nHit Return to return to main menu')

    return

# C. 2. Display record from database function

def displaydb ():

    os.system ('cls')

    key =  checkdecimal ('Student Number: ' , 'Decimal digits')
    module = checkmod ('Module: ' , 'Module Format: CE1234')

    try: # Check if database exists
        file = open (module, 'r')
    except:
        print ("Unable to read database %s" % module)
        exit(1)
        file.close ()

    db = open (module)

    if key in db:
        data = db[key]
        List1 = data.split()

        os.system('cls')
        print ("Student Details")
        print ("_______________\n")
        print ("Number:     %s" % List1 [0])
        print ("Title:      %s" % List1 [1])
        print ("Forname:    %s" % List1 [2])
        print ("Surname:    %s" % List1 [3])
        print ("Module:     %s" % List1 [4])
        print ("Coursemark: %s" % List1 [5])
        print ("Exammark:   %s" % List1 [6])
    else:
        print ('')
        print ("Student '%s' does not exist" % key)

    db.close ()

    print ('')
    key = input ('\n\nHit Return to return to main menu')

    return

# C. 3. Update an existing record of the database

def updatedb ():

    os.system ('cls')

    key =  checkdecimal ('Student Number: ' , 'Decimal digits')
    module = checkmod ('Module: ' , 'Module Format: CE1234')

    try: # Check if database exists - Not working!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        file = open (module, 'r')
    except:
        print ("Unable to read database %s" % module)
        exit(1)
        file.close ()

    db = open (module)

    if key in db:
        data = db [key]
        List1 = data.split()

        os.system('cls')
        print ("Student Details")
        print ("_______________\n")
        print ("Number:     %s" % List1 [0])
        print ("Title:      %s" % List1 [1])
        print ("Forname:    %s" % List1 [2])
        print ("Surname:    %s" % List1 [3])
        print ("Module:     %s" % List1 [4])
        print ("Coursemark: %s" % List1 [5])
        print ("Exammark:   %s" % List1 [6])

        print ('\nWhen promted for new values, hit Return to return value\n')

        title = checkalpha ('Title: ', 'Alphabetic characters')
        if title != '':
            List1 [1] = title

        forename = checkalpha ('Forename: ', 'Alphabetic characters')
        if forename != '':
            List1 [2] = forename

        surname = checkalpha ('Surname: ', 'Alphabetic characters')
        if surname != '':
            List1 [3] = surname

        coursemark = checkdecimal ('Coursemark: ', 'Decimal digits')
        if coursemark != '':
            List1 [5] = coursemark

        exammark = checkdecimal ('Exammark: ', 'Decimal digits')
        if exammark != '':
            List1 [6] = exammark

        data = ' '.join(List1)
        db [key] = data
        print ("\nStudent '%s' record has been updated" % key)

    else:
        print ('')
        print ("Student '%s' does not exist" % key)

    db.close ()

    print ('')
    key = input ('\n\nHit Return to return to main menu')

    return

# C. 4. Delete an existing record of the database

def deletedb ():

    os.system ('cls')

    key =  checkdecimal ('Student Number: ' , 'Decimal digits')
    module = checkmod ('Module: ' , 'Module Format: CE1234')

    try: # Check if database exists
        file = open (module, 'r')
    except:
        print ("Unable to read database %s" % module)
        exit(1)
        file.close ()

    db = open (module)

    if key in db:
        data = db [key]
        List1 = data.split()

        os.system('cls')
        print ("Student Details")
        print ("_______________\n")
        print ("Number:     %s" % List1 [0])
        print ("Title:      %s" % List1 [1])
        print ("Forname:    %s" % List1 [2])
        print ("Surname:    %s" % List1 [3])
        print ("Module:     %s" % List1 [4])
        print ("Coursemark: %s" % List1 [5])
        print ("Exammark:   %s" % List1 [6])

        while True:
            answer = input ('\nDelete (Y/N): ')
            if answer == 'Y' or answer == 'N':
                break
        
        if answer == 'Y':
            del db[key]
            print ("Student '%s' has been deleted" % key)
        else:
            print ("Student '%s' " % key, "has not been deleted")
    
    else:
        print ('')
        print ("Student '%s' does not exist" % key)

    db.close ()
    
    print ('')
    key = input ('\n\nHit Return to return to main menu')

    return

# C. 5. Display a list of student on a specific module 

def displayrec ():

    os.system ('cls')

    module = checkmod ('Module: ' , 'Module Format: CE1234')

    try: # Check if database exists
        file = open (module, 'r')
    except:
        print ("Unable to read database %s" % module)
        exit(1)
        file.close ()

    db = open (module)

    print ("List of students on module %s" % module)
    print ("")
    print ("Name                        Mark")
    print ("¯¯¯¯                        ¯¯¯¯")
    
    for key in db:
        data = db [key]
        List1 = data.split ()
        final_mark = int (List1 [5]) + int (List1 [6])
        details = List1 [1] + ' ' + List1 [2] + ' ' + List1 [3]
        
        print ('%-28s %3d' % (details , final_mark))
    db.close ()

    print ('')
    key = input ('\n\nHit Return to return to main menu')

    return

# D. Main Menu

# Printing following menu:
# Module Records
# (1) Add a record
# (2) Display a record
# (3) Update a record
# (4) Delete a record
# (5) Display the details of all students on the module
# (6) Exit
#
# Select option:-

while True:

    # Clear command line for every loop
    import os
    os.system ('cls')

    print ("    Module Records")
    print ("")
    print ("(1) Add a record")
    print ("(2) Display a record")
    print ("(3) Update a record")
    print ("(4) Delete a record")
    print ("(5) Display the details of all the students on the module")
    print ("(6) Exit")
    print ("")

    # Selection input can only be an integer between (1) and (6)
    selection = input ("Select option:-")

    if selection == '1':
        addtodb ()

    elif selection == '2':
        displaydb ()

    elif selection == '3':
        updatedb ()

    elif selection == '4':
        deletedb ()

    elif selection == '5':
        displayrec ()

    elif selection == '6':
        break

    else:
        print ('Invalid option')
        key = input ('\n\nHit Return to return to main menu')

os.system ('cls')
print ('')
print ('See you later')