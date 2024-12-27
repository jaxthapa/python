print("please enter your details details below!!")

name = input("Enter your full name:")
level = input("Enter your level:")
english = float(input("marks obtained in english:"))
mathematics =float(input("marks obtained in mathematics:"))
science =float(input("marks obtained in science:"))

total_marks_obtained =(english+mathematics+science)
average_of_all_subjects = ((english+mathematics+science)/3)

print("------------------------------------------------")
print("TOTAL AND AVERAGE")
print("Name:", name)
print("Level:", level)
print(f"Total marks obtained:", total_marks_ontained)
print(f"Average:{average_of_all_subjects: .1f}")




