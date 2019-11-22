#! /usr/bin/env python3.6
## File : Crowd Funding Donating System 
## Author : Eslam Roshdi 
## Email : e.roshdii@gmail.com
## Date : 21 Nov 2019
## Info : e.g kick starter 
## Course : Intro to python
## Instructor : Abd Arahman Hamdy 

import os 
from checking_funcs import *
from menu_class import MENU

db_dir = "db"
user_file = "user.csv"
proj_file = "proj.csv"
dont_file = "dont.csv"

user_file_header = ['id','name','email','pswd']
proj_file_header = ['id','name','u_id','total','donats']
dont_file_header = ['id','p_id','u_id','amount']

class User:
	# List of Users
	# add user , delete, edit, view 

	users = []
	no_of_users = 0
	menu = MENU(['View Info','Edit info','Delete Account'])
	edit_menu = MENU(['name','email','password'])

	def __init__(self,id,name,email,pswd):
		# check values & assign
		# add(self)
		print("construct user")
		self.id = id  
		self.name = name 
		self.email = email 
		self.pswd = pswd
		self.projects = []
		self.donations = []
	
	@classmethod
	def add(cls,**kwargs):
		# append(self) to list 
		# recursive update 
		print("user add")
		if len(kwargs) == 0 :
			tmp_dic = {
				'id' : (cls.no_of_users+1) ,
				'name' : input("Enter name : "),
				'email' : input("Enter email : "),
				'pswd' : input("Enrer password : "),
				# 'age' : input("Enter age")
				# 'gender' : input("Enter gender")
				# 'counter' : input ("Enter country")
			}
		else :
			tmp_dic = kwargs 

		for obj in cls.users :
			if obj.email == tmp_dic['email'] :
				return -1 

		X = cls(**tmp_dic) ; 
		cls.users.append(X)
		cls.no_of_users += 1
		cls.recursive_update_users()
		return X 
	

	def edit(self):
		print("user edit")
		# display all info
		# edit whatever 
		# recursive update 
		while True :
			clear_screen()
			self.view()
			x = User.edit_menu.draw()
			if x == 1 :
				self.name = input("Enter new name : ")
			elif x == 2 : 
				self.email = input("Enter new email : ")
				# consider change to a preserved one 
			elif x == 3 : 
				self.pswd = input("Enter new password : ")
			elif x == 0 :
				break ;
			else : 
				print("invalid")
		User.recursive_update_users()

	def delete(self):
		print("user delete")
		# remove user obj from list 
		# recursice update 
		if input("Are you sure to delete you Account ?[Y/N]") == 'Y' :
			x = input("Enter your password : ")
			if x == self.pswd :
				User.users.remove(self)
				cls.recursive_update_users()
				input("Account Removed")

			else :
				input("Invalid password ")

	def view(self):
		print("user view")
		# display current user info
		print("ID : ",self.id)
		print("Name : ",self.name)
		print("Email : ",self.email)


	@classmethod
	def login(cls,email,psw):
		print("user select")
		# search for user with email 
		# check for psw 
		# return user obj if ok 
		# return -1 if not ok
		for obj in cls.users:
			if obj.email == email and obj.pswd == psw :
					return obj
		return -1 
	########### FILE ######################
	@classmethod
	def recursive_read_users(cls):
		print("users recursive read ")
		# check db file is exit if not make a new 
		# read users file db 
		# convert to user obj 
		# append obj to users list 
		check_file(db_dir,user_file,user_file_header)
		with open(db_dir+'/'+user_file,'r') as file :
			txt_reader = csv.DictReader(file)
			for line in txt_reader :
				usr = dict(line)
				cls.add(**usr)

	@classmethod
	def recursive_update_users(cls):
		print("users recursive update ")
		# check db file is exit if not make a new 
		# loop users list 
		# convert from obj to dict 
		# write to users file 
		check_file(db_dir,user_file,user_file_header)
		with open(db_dir+'/'+user_file,'w') as file :
			txt_writer = csv.DictWriter(file,fieldnames=user_file_header)
			txt_writer.writeheader()
			for obj in cls.users:
				tmp_dic = {
					'id' : obj.id,
					'name':obj.name,
					'email':obj.email,
					'pswd':obj.pswd,
				}
				txt_writer.writerow(tmp_dic)



class Project:
	# List of Projects 
	# Start Project (with st.date / end.date) 
	# End Project (check donation 25% reached)

	projects = []
	no_of_projects = 0 
	menu = MENU(['Add Project','donate projct','Edit Project','Delete Project','View project','View Project of user','View Projects by date','View All Projects'])

	def __init__(self,id,name,u_id,total=0,donats=0):
		print("construct project ")
		# check_values & assign them 
		# start project 
		self.id = id
		self.name = name 
		self.u_id = u_id
		self.total = total
		self.donats = donats 
		

	@classmethod
	def add(cls,**kwargs):
		print("add project ")
		# take values 
		# append to list 
		# recursive update project file 
		 
		for obj in cls.projects :
			if obj.id == kwargs['id'] :
				input("Project found before !!")
				return -1 

		X = cls(**kwargs)
		cls.projects.append(X)
		cls.no_of_projects += 1 
		cls.recursve_update_projects()
		return X 

	@classmethod
	def start(cls,u_id,name=None):
		print("project start")
		# recieve info about project from user 
		if name == None : 
			name = input("Enter projct name : ") 
		tmp_dic = {
			'id' : cls.no_of_projects+1 ,
			'name' : name ,
			'u_id' : u_id,
			'total' : 0 ,
			'donats' : 0 ,
		}
		cls.add(**tmp_dic)

	def donate(self):
		print("project donate")
		# construct donate with id of user & project

	def edit(self):
		print("project edit")
		# edit details of project 
		# recursive update 

	def end(self):
		print("project end")
		# check 25% off and time not passed
		# remove project from list
		# recursive update project file

	def view(self):
		projects("projct view")
		# print all attribuites of this project 
		print("ID : ",self.id)
		print("Name : ",self.name)
		print("User/Creator ID : ", self.u_id)
		print("User/Creator Name : " , User.users[self.u_id].name )
		print("Total needed donations : ",self.total)
		print("Current donats : ",self.donats)


	###### Out Sourceing Searching #######
	@classmethod
	def projects_of_user(cls,user_id):
		print("projects of user")
		# display all projects for specific user

	@classmethod
	def projects_of_time(cls,st_date,end_date):
		print("projects of time ")
		# display all projects(may inc. donats) within time search 

	@classmethod
	def all_projects(cls):
		print("all projects ")
		# display all projects 

	########### FILE ######################
	@classmethod
	def recursive_read_projects(cls):
		print("projects recursive read")
		# check db file is exit if not make a new 
		# read projects file db 
		# convert to project obj 
		# append obj to projects list 
		check_file(db_dir,proj_file,proj_file_header)
		with open(db_dir+'/'+proj_file,'r') as file :
			txt_reader = csv.DictReader(file)
			for line in txt_reader :
				pro = dict(line)
				cls.add(**pro)

	@classmethod
	def recursve_update_projects(cls):
		print("projects recursive update")
		# check db file is exit if not make a new 
		# loop projctss list 
		# convert from obj to struct 
		# write to projects file 
		check_file(db_dir,proj_file,user_file_header)
		with open(db_dir+'/'+proj_file,'w') as file :
			txt_writer = csv.DictWriter(file,fieldnames=proj_file_header)
			txt_writer.writeheader()
			for obj in cls.projects:
				tmp_dic = {
					'id' : obj.id,
					'name':obj.name,
					'u_id':obj.u_id,
					'total':obj.total,
					'donats':obj.donats,
				}
				txt_writer.writerow(tmp_dic)

class Donation:
	# List of donations 
	# add a donate with the project id & user id donating 
	# remove a donate (at specfic project / from login user)
	
	dontas = []
	no_of_donats = 0 
	menu = MENU(['add','donates of user','donats on project'])

	def __init__(self,donate_id,user_id,project_id):
		print("construct donate")
		if donate_id == None :
			donate_id = no_of_donats + 1  
		# check & assign values to current donation
		# add (self)

	def add(self):
		print("donat add ")
		# append donate_obj to list 
		# recursive update donate file 

	def remove(Self):
		print("donat remove")
		# remove donate with id from list 
		# recursive update donate file


	########## out sourceing search ####################
	@classmethod 
	def donats_of_user(cls,user_id):
		print("donats of user")
		#search for all donats with user_id 
		#display donats and prespective projects

	@classmethod
	def donats_on_project(cls,project_id):
		print("donats on project")
		#search for all donats with project_id 
		#display donats and prespective user 

	########### FILE ######################
	@classmethod
	def recursive_read_donats(cls):
		print("donats recursrive read")
		# check db file is exit if not make a new 
		# read donate file db 
		# convert to donate obj 
		# append obj to donats list 

	@classmethod
	def recursve_update_donats(cls):
		print("donats recursrive update ")
		# check db file is exit if not make a new 
		# loop donats list 
		# convert from obj to struct 
		# write to donate file 

def Signup():
	print("Sign up ")
	#1 Get Info from user(check if valid) 
	#2 Add USer (check return is ok)
	#3 Re #1 if not ok 
	#4 Back to main 
	if User.add() == -1 :
		input("User found before !! [try to login]")
	else :
		input("Sucessfully SignUp .. try to login")
	
def Login():
	print("Log in")
	
	errs = 0 
	
	while True :
		clear_screen()
		email = input("Enter your valid email : ")
		ps = input("Enter your password : ")
		loged_user = User.login(email,ps)
		if loged_user == -1 :
			errs += 1 
			if errs >= 3 :
				input("3 Invalid Attempts :: Account Locked !!! ")
				return -1 ; 
			if '0' == input("Invalid login [press to try agian /or/ 0 to exit] : "+"\n"):
				return 0
		else :
			input("Successfully login Hi "+loged_user.name)
			break 

	
	while True :			
		clear_screen()
		re1 = acco_menu.draw()
		if re1 == 1 :
			while True :
				clear_screen()
				re2 = User.menu.draw()
				if re2 == 1 :
					loged_user.view()
					input("Enter any key to continue ")
				elif re2 == 2 :
					loged_user.edit()
				elif re2 == 3 :
					loged_user.delete()
					return ;
				elif re2 == 0 :
					break;
				else :
					print("Invalid ")

		elif re1 == 2 :
			tmp_pr = Project.select(loged_user.id)
			while True :
				clear_screen()
				re2 = Project.menu.draw()
				if re2 == 1 : 
					tmp_pr.start()
				elif re2 == 2 :
					tmp_pr.donate()
				elif re2 == 3 :
					tmp_pr.edit()
				elif re2 == 4 : 
					tmp_pr.end()
				elif re2 == 5 :
					tmp_pr.view()
				elif re2 == 6 :
					Project.projects_of_user(1)
				elif re2 == 7 : 
					Project.projects_of_time(1)
				elif re2 == 8 :
					Project.all_projects()
				elif re2 == 0 :
					break;
				else :
					print("Invalid ") 


		elif re1 == 3 :
			print("Sign out")
			break;

		else :
			print("invalid")
	#1 check email/pass for user >> if true login_user is selected  
	#2 User menu : Account settings , Projects , Donations , Signout
	#3 Account Setting menu : Edit Info , Delete Account 
	#4 Project Menu : Add project(with data) , view projects(user/all/data) , edit project , Delete project , 
	#5 Donation Menu : project list (donate project / delete donate )
	#6 Sign Out 

main_menu = MENU(['Signup','Login','Exit'])
acco_menu = MENU(['Account','Projects','Signout'])

def main():
	
	#1 main menu : Signup , login 
	#2 signup > go for signup 
	#3 login > go for login 
	#4 Exit 
	check_dir(db_dir)
	User.recursive_read_users()
	Project.recursive_read_projects()

	while True :
		clear_screen()
		re1 = main_menu.draw()
		if re1 == 1 :
			Signup()
		elif re1 == 2 :
			if Login() == -1 :
				return -1
		elif re1 == 3 :
			return 0 ; 
		else :
			print("Invalid")

if __name__ == "__main__":
	main()
