from dbhelper import DBHelper

def main():
	db=DBHelper()
	while True:
		print("")
		print("*********Welcome*********")
		print("")
		print("Press 1 to insert new user")
		print("Press 2 to display all users")
		print("press 3 to update user")
		print("press 4 to delete user")
		print("press 5 to exit program")
		print()
		try:
			choice = int(input())
			if (choice==1):
				print("Please enter the id of the user:")
				ID=int(input())
				print("Enter name:")
				name= input()
				print("Enter phone number:")
				phone=input()
				db.insert_user(ID,name,phone)
				pass
			elif choice==2:
				db.fetch_all()
				pass
			elif choice==3:
				print("Enter the id of user to be updated:")
				ID=int(input())
				print("Enter the new name of the user:")
				name = input()
				print("Enter new phone number of user:")
				phone = input()
				db.update_user(ID,name,phone)
				pass
			elif choice==4:
				print("Enter the user id to be deleted:")
				ID = int(input())
				db.delete_user(ID)
				pass
			elif choice==5:
				break;
			else:
				print("Invalid Input ! Try again")
				print("")
		except Exception as e:
			print(e)
			print("Invalid details ! Try again")
			print("")

if __name__=="__main__":
	main()