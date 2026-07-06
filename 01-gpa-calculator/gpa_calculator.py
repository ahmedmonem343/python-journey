#calculating the avarage GPA

subjects = int(input("Please Enter the number of subjects : "))
total =0
for i in range (subjects):
    mark = float(input(f"enter the subject mark {i+1}: "))
    total+=mark
average = total/subjects 

#print(f"the GPA is: ", avarage)

if average >= 90:
    print(f"The GPA is: {average:.2f} - Grade: Excellent")
    

elif average >= 80:
    print(f"The GPA is: {average:.2f} - Grade: Very Good")  

elif average >= 70:
   print(f"The GPA is: {average:.2f} - Grade: Good")

elif average >= 60: 
   print(f"The GPA is: {average:.2f} - Grade: Pass") 

else:
   print(f"The GPA is: {average:.2f} - Grade: Fail")