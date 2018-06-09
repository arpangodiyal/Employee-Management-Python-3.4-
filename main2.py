import d
import os

print("1. Create a employee")
print("2. Retrieve records")
print("3. Update an employee")
print("4. Delete an employee")
print("5. Search an employee")
print("6. Exit")

choice=input("Enter your choice: ")
while choice!=6:
	if choice=='1':
		d.create()
	elif choice=='2':
		d.retrieve()
	elif choice=='3':
		d.update()
	elif choice=='4':
		d.delete()
	elif choice=='5':
		d.search()
	else:
		break
	input("Press any key to continue")
	os.system("cls")
	print("1. Create a employee")
	print("2. Retrieve records")
	print("3. Update an employee")
	print("4. Delete an employee")
	print("5. Search an employee")
	print("6. Exit")
	choice=input("Enter your choice: ")
