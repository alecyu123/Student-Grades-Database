inp = input("""Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
    1- Enter student records (Name, ID, and 6 marks separated by commas)
    2- Display the class average.
    3- Display the information for a given student
    4- List the entire class by name and ID.
    X- Exit
Select an option by entering its number or X to exit: """)

students = [] # Creates a list outside the while loop to save the data 
ident = [] # If the student record is valid, it will copy its identification number here to make sure no duplicates will appear
           # However, this assumes that the students list is empty at the start (which it's supposed to be) since it can't check the ID
           # numbers inside that list and instead adds the IDs to ident at the same time the tuple is added to students.
while inp != "X": # Creates a loop until user inputs X
    if inp == "1":
        lst = input("Enter student record (separate fields by commas) or done: ")
        while lst != "done": # Creates a loop until user inputs done
            splitlst = lst.split(",") # Seperates the string at comma; assumes no spaces before or behind it to create a list
            def check_digit(y): # Creates a function to help check if last 7 entries of list are natural numbers
                for x in range(1, len(y)):
                    if not y[x].isdigit():
                        return False
                return True
            is_it_splitlist = check_digit(splitlst)
                
            if len(splitlst) != 8: # Checks if it is the correct length
                if len(splitlst) < 8:
                    print("Record incomplete. Record rejected.")
                else:
                    print("Record invalid. Record rejected.")
                lst = input("Enter student record (separate fields by commas) or done: ")
            elif len(splitlst) == 8 and splitlst[0].isalpha() and int(splitlst[1]) not in ident and is_it_splitlist: # Checks for a valid
                                                                                                                     # entry
                for i in range(1, len(splitlst)): # Transforms all string digits to integers
                    splitlst[i] = int(splitlst[i])
                ident.append(splitlst[1]) # Copies identification number to ident
                splitlst = tuple(splitlst)
                students.append(splitlst) # Copies record to students
                lst = input("Enter student record (separate fields by commas) or done: ")
            elif splitlst[1].isdigit() and int(splitlst[1]) in ident: # Checks to see if there are duplicates with ident
                print("Duplicate ID number. Record rejected.")
                lst = input("Enter student record (separate fields by commas) or done: ")
            else: 
                print("Record invalid. Record rejected.") # Error message instead of crashing
                lst = input("Enter student record (separate fields by commas) or done: ")
            
    elif inp == "2":
        if len(students) == 0: # Ensures no division by zero/no crashing
            print("Please go to option 1 and add a student record")
        else:
            scores_class = [] # 2D List that contains the individual test scores of every individyal
            for seq in students: 
                scores_class.append(seq[2:8])
            total = 0
            for data in scores_class: # Decomposes the 2D list into the sum of all its values
                for value in data:
                    total += value
            avg = round(total/len(students))
            print("Class average is", avg)

    elif inp == "3":
        info_id = input("Enter the ID of the student: ")
        IDs = [] 
        for seq in students:
            IDs.append(seq[1])
        if info_id.isdigit() == False or int(info_id) not in ident: # Again, uses ident; thus assumes that students is an empty list at
                                                                    # the start; would not work otherwise
            print("Please enter a valid ID or go back to option 1 to make another entry")
        else:
            info_id = int(info_id)
            for seq in students:
                if seq[1] == info_id: # Searches students for the right ID
                    stname = seq[0]
                    stgrade = sum(seq[2:8])
                    break
                    
            if stgrade >= 87: # Converts numerical grades to letter grades
                letter = "A"
            elif stgrade >= 75:
                letter = "B"
            elif stgrade >=65:
                letter = "C"
            else:
                letter = "F"
            print("Information for", stname, info_id, "total grade", stgrade, "letter grade", letter)
    elif inp == "4":
        if len(students) == 0:
            print("Please go to option 1 and add a student record")
        else:
            stname_and_id = [] 
            for seq in students: 
                stname_and_id.append([seq[0], seq[1]]) # Creates list for student names and their id, in this order respectively to sort them
            stname_and_id.sort()
            for row in stname_and_id: # Sorts list according to student names (alphabetically); does not account for lowercase
                print(row[0], row[1])
    else:
        print("Please enter a valid option") # Error message to protect code from crashes
    
    inp = input("""Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
        1- Enter student records (Name, ID, and 6 marks separated by commas)
        2- Display the class average.
        3- Display the information for a given student
        4- List the entire class by name and ID.
        X- Exit
    Select an option by entering its number or X to exit: """)
       

        