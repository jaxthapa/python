#Calculating the average marks and grand total with percentages

name= input("Enter your name:")
#Storing marks
math=int(input("Enter the marks of math"))
science =int(input("Enter the marks of science"))
english=int(input("Enter the marks of english"))
nepali=int(input("Enter the marks of nepali"))


total = sum([math, science, english, nepali])
average =sum([math, science, english, nepali])/4
print(f"Hello {name}!! \n Your Grand Total Marks is: {total} And \n Average marks is: {average}")

      




