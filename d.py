import mysql.connector
def update():
	con=mysql.connector.connect(host="localhost",user="root",password="arpan",database="employee")
	cursor=con.cursor()
	print("enter the id to be updated")
	i=int(input())
	query="select * from table1 where id="+str(i)
	cursor.execute(query)
	row=cursor.fetchone()
	print(" ID :",row[0],"\n","Name :",row[1],"\n","Gender :",row[2],"\n","Salary",row[3],"\n","Department :",row[4],"\n")
	print("Enter the data to be updated")
	i=int(input("Enter id :"))
	n=input("Enter name :")
	g=input("Enter gender :")
	s=int(input("Enter salary :"))
	d=input("Enter department: ")
	print()
	query="update table1 set name='"+n+"',id="+str(i)+",gender='"+g+"',salary="+str(s)+",dept='"+d+"' where id="+str(i)
	cursor.execute(query)
	query="select * from table1 where id="+str(i)
	cursor.execute(query)
	row=cursor.fetchone()
	print("Employee updated succesfully")
	print(" ID :",row[0],"\n","Name :",row[1],"\n","Gender :",row[2],"\n","Salary",row[3],"\n","Department :",row[4],"\n")
	con.commit()
	cursor.close()

def create():
	con=mysql.connector.connect(host="localhost",user="root",database="employee",password="arpan")
	cursor=con.cursor()
	i=int(input("Enter id :"))
	n=input("Enter name :")
	g=input("Enter gender :")
	s=int(input("Enter salary :"))
	d=input("Enter department :")
	query="insert into table1 values("+str(i)+",'"+n+"','"+g+"',"+str(s)+",'"+d+"')"
	cursor.execute(query)
	print("Employee saved")
	con.commit()
	cursor.close()

def retrieve():
	con=mysql.connector.connect(host="localhost",user="root",database="employee",password="arpan")
	cursor=con.cursor()
	print()
	query="select * from table1 order by id"
	no=1
	cursor.execute(query)
	row=cursor.fetchone()
	flength=[2,4,6,6,10]
	while row is not None:
		length=[len(str(row[0])),len(row[1]),len(row[2]),len(str(row[3])),len(row[4])]
		
		for i in range(5):
			if length[i]>flength[i]:
				flength[i]=length[i]
		row=cursor.fetchone()
		no=no+1
	query="select * from table1 order by id"
	cursor.execute(query)
	row=cursor.fetchone()
	dlen=len("ID"+" "*(flength[0]-len("ID")+1)+"Name"+" "*(flength[1]-len("Name")+1)+"Gender"+" "*(flength[2]-len("Gender")+1)+"Salary"+" "*(flength[3]-len("Salary")+1)+"Department"+" "*(flength[4]-len("Department")+1))+flength[4]-len("Department")+4
	lengths=[flength[0]+len("ID"+" "*(flength[0]-len("ID")+1)),flength[1]+len("Name"+" "*(flength[1]-len("Name")+1)),flength[2]+len("Gender"+" "*(flength[2]-len("Gender")+1)),flength[3]+len("Salary"+" "*(flength[3]-len("Salary")+1)),flength[4]+len("Department"+" "*(flength[4]-len("Department")+1)),flength[4]-len("Department")+4]
	l=0
	for j in range(5):
		lengths[j]=flength[j]+l+2
		l=lengths[j]+1
	for i in range(dlen+4):
		if i in lengths:
			print("+",end="")
		else:
			print("-",end="")

	print()
	print("ID"," "*(flength[0]-len("ID")),"|Name"," "*(flength[1]-len("Name")),"|Gender"," "*(flength[2]-len("Gender")),"|Salary"," "*(flength[3]-len("Salary")),"|Department"," "*(flength[4]-len("Department")))
	for i in range(dlen+4):
		if i in lengths:
			print("+",end="")
		else:
			print("-",end="")
	while row is not None:
		print()
		print(row[0]," "*(flength[0]-len(str(row[0]))),"|"+row[1]," "*(flength[1]-len(row[1])),"|"+row[2]," "*(flength[2]-len(row[2])),"|"+str(row[3])," "*(flength[3]-len(str(row[3]))),"|"+row[4]," "*(flength[4]-len(row[4])))
		for i in range(dlen+4):
			if i in lengths:
				print("|",end="")
			else:
				print("-",end="")
		row=cursor.fetchone()
	print()
	cursor.close()

def delete():
	con=mysql.connector.connect(host="localhost",user="root",password="arpan",database="employee")
	cursor=con.cursor()
	print("Enter the id to be deleted")
	i=int(input())
	query="select * from table1 where id="+str(i)
	cursor.execute(query)
	row=cursor.fetchone()
	while row is not None:
		print(" ID :",row[0],"\n","Name :",row[1],"\n","Gender :",row[2],"\n","Salary",row[3],"\n","Department :",row[4],"\n")
		row=cursor.fetchone()
		print(2*"\n")
	print("Enter yes to delete the record")
	choice=input()
	if choice=='yes':
		query="delete from table1 where id="+str(i)
		cursor.execute(query)
		con.commit()
		print("Employee has been deleted")
		cursor.close()
	else:
		cursor.close()

def search():
	print("Enter the ID for employee to be searched")
	i=int(input())
	con=mysql.connector.connect(host="localhost",user="root",password="arpan",database="employee")
	cursor=con.cursor()
	query="select * from table1 where id="+str(i)
	cursor.execute(query)
	row=cursor.fetchone()
	if row is None:
		print("Employee not found")
	else:
		while row is not None:
			print(" ID :",row[0],"\n","Name :",row[1],"\n","Gender :",row[2],"\n","Salary",row[3],"\n","Department :",row[4],"\n")
			row=cursor.fetchone()
			print()
	cursor.close()


	


