names = []

grades = []

while True:

    print("\n===== Student Gradebook =====")
    print("1- Add Student ")
    print("2- Show All Student")
    print("3- Search Student")
    print("4- Remove Students")
    print("5- Show Class Average")
    print("6- Exit")

    choice = input ("Chose an opetion: ")
    print(choice)
    print(type(choice))
     
    

    
    if choice == "1":
        name = input("Enter student name: ").strip().title()

        grade = float(input("Enter student grade: "))

        names.append(name)

        grades.append(grade)

        print(f"{name} added successfully with grade {grade}.")



    elif choice == "2":
       if len(names) == 0:
           print("no students found. ")

       else:
           print("\n===== Students =====")
           for i in range(len(names)):
               print(f"{i+1} - {names[i]} - {grades[i]}")
           

       
    
       


   
    elif choice == "3":
        search_name = input("Enter Student name: ").strip().title()
        found = False
        for i in range (len(names)):
            if search_name == names[i]:
                print ("Student found")
                print (f"Name : {names[i]}")
                print (f"Grade: {grades[i]}")

                found = True
                break
        if not found:
            print("Student not found. ")

    
    elif choice == "4":
        print("Remove student selected")



    elif choice == "5":
        print("Show student selected")



    elif choice == "6":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. please choose from 1 to 6.")