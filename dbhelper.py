import mysql.connector as connector

class DBHelper:
	def __init__(self):
		self.con=connector.connect(host='localhost',
									port='3306',
									user='root',
									password='root',
									database='pythontest')
		query='create table if not exists user(userID int primary key,userName varchar(200), phone varchar(12))'
		cur = self.con.cursor()
		cur.execute(query)
		print("Created")

	def insert_user(self, userID, userName, phone):
		query = "insert into user(userID,userName,phone) values({},'{}','{}')".format(userID,userName,phone)
		#print(query)
		cur=self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("User saved")
		print("")


	def fetch_all(self):
		query = "select * from user"
		curr = self.con.cursor()
		curr.execute(query)
		for row in curr:
			print("")
			print("userID :",row[0])
			print("userName :",row[1])
			print("Phone :",row[2])
		print("")


	def delete_user(self,userID):
		query = "delete from user where userID= {}".format(userID)
		curr=self.con.cursor()
		curr.execute(query)
		self.con.commit()
		print("deleted")
		print("")

	def update_user(self,userID,newName,newPhone):
		query = "update user set userName='{}', phone='{}' where userID= {}".format(newName,newPhone,userID)
		curr = self.con.cursor()
		curr.execute(query)
		self.con.commit()
		print("User updated")
		print("")
