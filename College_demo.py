#1_20260901.docx Set_Enrollment.docx
"""
College Management System

Write a menu-driven Python script which allows the user to perform the following operations.

Add College – Allow users to enter details of a college such as college code, college name, rating, and location.


Display All Colleges – Display all college details in sorted order (sorting by code or name).


Display Colleges by Location – Allow users to enter a location and display colleges of that location.


Display College with Highest Rating – Display details of the college having the highest rating.

"""
print("College Managment System")
colleges={
101:{'code':101,'cname':"FCAIT",'rating':2,'loc':'Ahmedabad'},
102:{'code':102,'cname':"Parul",'rating':4,'loc':'Baroda'}
		 }

def display():
	for c in colleges:
		print("College Code:",colleges[c]['code'])
		print("College Name:",colleges[c]['cname'])
		print("College Ratting:",colleges[c]['rating'])
		print("College Location:",colleges[c]['loc'])

def searchloc():
	sloc=input("Enter college Location")
	for c in colleges:
		if colleges[c]['loc']==sloc:
			print("College Code:",colleges[c]['code'])
			print("College Name:",colleges[c]['cname'])
			print("College Ratting:",colleges[c]['rating'])
			print("College Location:",colleges[c]['loc'])

def deletecol():
	code= int(input("Enetr College Code"))
	del colleges[code]
	print("College Deleted")

def highest():
	high=0
	for c in colleges:
		if colleges[c]['rating']>high:
			high= colleges[c]['rating']
			hcol=c

	print("Highest Rated College",colleges[hcol]['cname'])

def addCollege():
	code=int(input("Eneter College Code"))
	if code in colleges.keys():
		print("College Code is already Used")
		code=int(input("Eneter New College Code"))
	cname=input("Eneter College Name")
	rating=int(input("Eneter College rating"))
	loc=input("Eneter College Location")
	colleges[code]={'code':code,'cname':cname,'rating':rating,'loc':loc}

while True:
	print("1 for Add New College")
	print("2 for Display All College")
	print("3 for Search College by Location")
	print("4  College with Highest Rank")
	print("0 for Exit")

	choice= int(input("Enter Choice (0-4)"))

	if choice==1:
		print("Add College-:")
		addCollege()
	if choice==2:
		print("Display All College-:")
		display()
	if choice==3:
		print("Search College-:")
		searchloc()
	if choice==4:
		print("Highest Rank College-:")
		highest()
	if choice==0:
		print("Exit :")
		break
